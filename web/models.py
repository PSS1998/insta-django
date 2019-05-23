from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=48)
    def __unicode__(self):
        return "{}_token".format(self.user)

class Account(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.username
