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
    url(r'^dashboard_add_account/', views.dashboard_add_account, name="dashboard_add_account"),
    url(r'^dashboard_edit_account/(?P<pk>\d+)/$', views.dashboard_edit_account, name="dashboard_edit_account"),
    url(r'^account_page/(?P<pk>\d+)/$', views.account_page, name="account_page"),
    url(r'^account_page/(?P<pk>\d+)/settings/$', views.setting, name="setting"),
    url(r'^$', views.index, name='index'),
]
