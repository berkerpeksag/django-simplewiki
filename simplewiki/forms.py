from __future__ import print_function, unicode_literals

from django import forms

from .models import Revision


class RevisionForm(forms.ModelForm):

    class Meta:
        model = Revision
        fields = ('content', 'summary')
