# Generated by Django 2.2.1 on 2019-05-29 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20190526_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_number', models.IntegerField()),
                ('unfollow_number', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Account')),
            ],
        ),
    ]
