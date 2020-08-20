from django import forms
from .models import People
from .models import User


class PeopleForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ('firstname', 'lastname')
        # exclude = ('lastname')