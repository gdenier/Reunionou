# Generated by Django 2.0.6 on 2018-07-06 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=600)),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('token', models.CharField(max_length=256)),
                ('auteur', models.CharField(max_length=80)),
                ('adresse', models.CharField(max_length=256)),
            ],
        ),
    ]