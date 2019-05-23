from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^submit/account/$', views.submit_account, name='submit_account')
]
