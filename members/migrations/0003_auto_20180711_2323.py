# Generated by Django 2.0.7 on 2018-07-11 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20180706_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='auteur',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
