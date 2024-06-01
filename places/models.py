from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=75)
    comments = models.TextField()
    latitude = models.FloatField(default=10.659190899078881)
    longitude = models.FloatField(default=106.72701745885105)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
