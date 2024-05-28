from django import forms
from . import models

class PlaceForm(forms.ModelForm):
    class Meta:
        model = models.Place
        fields = ['name', 'latitude', 'longitude', 'comments', ]
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }
