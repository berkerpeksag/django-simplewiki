from django import forms

from .models import Document, Revision
from .utils import create_diff


class DocumentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    class Meta:
        model = Document
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 70, 'rows': 20}),
        }

    def save(self, commit=True):
        obj = super().save(commit=commit)
        try:
            latest_content = self.instance.revisions.latest().content
        except Revision.DoesNotExist:
            latest_content = ''
        revision = Revision(
            document=self.instance, creator=self.user,
            content=self.instance.content, rendered=self.instance.rendered,
            diff=create_diff(latest_content, self.instance.content),
        )
        revision.save()
        return obj
