from django import forms
from django.forms.models import inlineformset_factory

from .models import Document, Revision


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ('title',)


class RevisionForm(forms.ModelForm):

    class Meta:
        model = Revision
        fields = ('content', 'summary')
        widgets = {
            'content': forms.Textarea(attrs={'cols': 70, 'rows': 20}),
        }

RevisionFormSet = inlineformset_factory(Document, Revision, form=RevisionForm,
                                        extra=1, can_delete=False)
