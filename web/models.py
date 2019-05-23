from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
