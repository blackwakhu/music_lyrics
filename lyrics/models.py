from django.db import models

# Create your models here.

class songs(models.Model):
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    lyrics = models.TextField()
