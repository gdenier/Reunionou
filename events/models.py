import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=600)
    date = models.DateTimeField('date published')
    token = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    addresse = models.CharField(max_length=256)
    public = models.BooleanField()

    def __str__(self):
        return self.title

class Guest(models.Model):
    last_name = models.CharField(max_length=80, null=True)
    first_name = models.CharField(max_length=80, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    email = models.CharField(max_length=80, null=True)
    password = models.CharField(max_length=80, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField('date published', auto_now_add=True)
    core = models.CharField(max_length=512)
    like = models.PositiveSmallIntegerField(default=0)
    dislike = models.PositiveSmallIntegerField(default=0)
    edited = models.DateTimeField('date edited', null=True)
    deleted = models.BooleanField(default=False)
    response_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

class Like_Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    com = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    value = models.BooleanField()

    def __str__(self):
        return self.value