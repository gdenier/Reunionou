# Generated by Django 2.0.6 on 2018-07-13 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20180713_1431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guest',
            old_name='user_id',
            new_name='user',
        ),
    ]