from django.db import models

# Create your models here.
class User(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=40)
    tags = models.CharField(max_length=255, default='')
    favourites = models.CharField(max_length=255, default='')