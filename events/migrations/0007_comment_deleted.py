# Generated by Django 2.0.6 on 2018-07-16 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_comment_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='deleted',
            field=models.BooleanField(default=None),
            preserve_default=False,
        ),
    ]
