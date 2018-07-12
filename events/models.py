import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    titre = models.CharField(max_length=256)
    description = models.CharField(max_length=600)
    date = models.DateTimeField('date published')
    token = models.CharField(max_length=256)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=256)
    public = models.BooleanField()

    def __str__(self):
        return self.titre

class Inviter(models.Model):
    nom = models.CharField(max_length=80)
    prenom = models.CharField(max_length=80)
    age = models.PositiveSmallIntegerField()