from django.db import models

# Create your models here.

class Project (models.Model):
    n_identification = models.IntegerField()
    stock = models.IntegerField()
    namep = models.CharField(max_length=20)