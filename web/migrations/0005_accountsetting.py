# Generated by Django 2.2.1 on 2019-05-26 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20190523_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Account')),
            ],
        ),
    ]
