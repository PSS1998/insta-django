from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Passwordresetcodes(models.Model):
    code = models.CharField(max_length=32)
    email = models.CharField(max_length=120)
    time = models.DateTimeField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)  # TODO: do not save password

class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)
    def __unicode__(self):
        return "{}_token".format(self.user)

class Account(models.Model):
    username = models.CharField(max_length=255, blank=False)
    password = models.CharField(max_length=255, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.username
