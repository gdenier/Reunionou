# Generated by Django 2.0.6 on 2018-07-16 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_comment_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
