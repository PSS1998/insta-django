from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.db import models
from django.contrib.auth.models import User
from django_mysql.models import ListCharField, ListTextField
from django.db.models import CharField, IntegerField, TextField

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
    def save(self,*args,**kwargs):
        created = not self.pk
        super().save(*args,**kwargs)
        if created:
            AccountSetting.objects.create(account=self)
            AccountReport.objects.create(account=self)

class AccountReport(models.Model):
    follow_number = models.IntegerField(default=0)
    unfollow_number = models.IntegerField(default=0)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

class AccountSetting(models.Model):
    active = models.BooleanField(default=True)
    like = models.BooleanField(default=False)
    comment = models.BooleanField(default=False)
    like_per_day = models.IntegerField(default=50)
    comments_per_day = models.IntegerField(default=25)
    tag_list = ListTextField(default=[], base_field=CharField(max_length=100), size=20,)
    tag_blacklist = ListTextField(default=[], base_field=CharField(max_length=100), size=20,)
    user_blacklist = ListTextField(default=[], base_field=CharField(max_length=100), size=20,)
    max_like_for_one_tag = models.IntegerField(default=25)
    follow_per_day = models.IntegerField(default=100)
    follow_time = models.IntegerField(default=3600)
    unfollow_per_day = models.IntegerField(default=25)
    comment_list = ListTextField(default=[], base_field=CharField(max_length=100), size=20,)
    unwanted_username_list = ListTextField(default=[], base_field=CharField(max_length=100), size=20,)
    unfollow_whitelist = ListTextField(default=[], base_field=CharField(max_length=100), size=20,)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    def __str__(self):
        return self.account.user.username
