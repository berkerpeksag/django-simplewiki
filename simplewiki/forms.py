from django import forms

from .models import Document


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 70, 'rows': 20}),
        }
