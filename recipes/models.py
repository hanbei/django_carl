from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Recipe(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=120, unique=True)
    rating = models.SmallIntegerField(default=0, unique=True)
