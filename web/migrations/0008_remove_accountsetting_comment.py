# Generated by Django 2.2.1 on 2019-05-26 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20190526_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountsetting',
            name='comment',
        ),
    ]