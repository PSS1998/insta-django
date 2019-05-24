from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^submit/account/$', views.submit_account, name='submit_account'),
    url(r'^edit/account/?$', views.edit_account, name='edit_account'),
    url(r'^accounts/register/?$', views.register, name='register'),
    url(r'^accounts/login/?$', views.login_auth, name='login'),
    url(r'^accounts/logout/?$', views.logout_auth, name='logout'),
    url(r'^accounts/reset_password/?$', views.reset_password, name='reset_password'),
    url(r'^dashboard/', views.dashboard, name="dashboard"),
    url(r'^$', views.index, name='index'),
]
