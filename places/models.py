from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Place(models.Model):
    name = models.CharField(max_length=75)
    comment = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
    