from django import forms

from .models import Revision


class RevisionForm(forms.ModelForm):

    class Meta:
        model = Revision
        exclude = ('rendered',)
