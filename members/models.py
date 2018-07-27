import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Message(models.Model):
    """
        Model for message between users

        Keyword:
        content -- the content of the message
            (string)
        date -- the date of redaction
            (datetime)
        author -- the author of the message
            (User)
        target -- the target of the message
            (User)
            (multiple)
    """
    content = models.CharField(max_length=600)
    date = models.DateTimeField('date published', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.ManyToManyField(User, related_name='targets')
    
