import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):
    """
        Model for event

        Keyword:
        title -- the title of the event
            (string)
        description -- a short or long description of the event
            (string)
        date -- the date for the event
            (datetime)
        token -- the token access to the event
            (string)
        author -- the promoter of the event
            (string)
        address -- the address of the event
            (string)
        public -- a boolean field to know if the event is public
            (boolean)
    """
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=600)
    date = models.DateTimeField('date published')
    token = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=256)
    public = models.BooleanField()

    def __str__(self):
        return self.title

class Guest(models.Model):
    """
        Model for Event's Guest

        Keyword:
        last_name -- the last name of the guest
            (string)
        first_name -- the first name of the guest
            (string)
        age -- the age of the guest
            (int)
        email -- the email of the guest
            (string)
        password -- the password of the guest
            (string)
            (Django's ash method)
        event -- the event which the guest in registered
            (Event)
        user -- can be the User who the guest is linked
            (User)
            (optional)
    """
    last_name = models.CharField(max_length=80, null=True)
    first_name = models.CharField(max_length=80, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    email = models.CharField(max_length=80, null=True)
    password = models.CharField(max_length=80, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Comment(models.Model):
    """
        Model for Event's Comment

        Keyword:
        author -- the author of the comment
            (string)
        date -- the date of the first edit
            (datetime)
            (default: now)
        core -- the content of the comment
            (string)
        like -- the number of like on this comment
            (int)
            (default: 0)
        dislike -- the number of dislike on this comment
            (int)
            (default: 0)
        edited -- the date of the last re-edit
            (if null -> no re-edit)
            (datetime)
            (default: Null)
        deleted -- a boolean field to know if the comment has been deleted
            (boolean)
            (default: False)
        response_to -- the comment which it has reponsed
            (if null -> it's not a response)
            (Comment)
            (optional)
        event -- the event wich the comment is linked
            (Event)

    """
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
    """
        Model for Like and Dislike on Event or on Comment

        Keyword:
        user -- the User linked to the like or dislike
            (User)
        com -- the Comment linked to the like or dislike
            (Comment)
            (optional)
        event -- the event linked to the like or dislike
            (Event)
            (optional)
        value -- True for a like and False for a dislike
            (boolean)
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    com = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    value = models.BooleanField()

    def __str__(self):
        return self.value