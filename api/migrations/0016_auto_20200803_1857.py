# Generated by Django 3.0.8 on 2020-08-03 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20200803_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user_name',
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ManyToManyField(to='api.User'),
        ),
    ]
