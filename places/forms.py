from django.forms import ModelForm
from . import models

class CreatePlace(ModelForm):
    class Meta:
        model = models.Place
        fields = ['name', 'comment', 'slug', 'banner']
