# Generated by Django 2.2.1 on 2019-05-26 12:47

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20190526_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsetting',
            name='comment',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='accountsetting',
            name='comment_list',
            field=django_mysql.models.ListTextField(models.CharField(max_length=100), default=[], size=20),
        ),
        migrations.AlterField(
            model_name='accountsetting',
            name='tag_blacklist',
            field=django_mysql.models.ListTextField(models.CharField(max_length=100), default=[], size=20),
        ),
        migrations.AlterField(
            model_name='accountsetting',
            name='tag_list',
            field=django_mysql.models.ListTextField(models.CharField(max_length=100), default=[], size=20),
        ),
        migrations.AlterField(
            model_name='accountsetting',
            name='user_blacklist',
            field=django_mysql.models.ListTextField(models.CharField(max_length=100), default=[], size=20),
        ),
    ]
