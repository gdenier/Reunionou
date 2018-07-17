# Generated by Django 2.0.7 on 2018-07-13 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('adresse', models.CharField(max_length=256)),
                ('public', models.BooleanField()),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inviter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=80, null=True)),
                ('prenom', models.CharField(max_length=80, null=True)),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('email', models.CharField(max_length=80, null=True)),
                ('password', models.CharField(max_length=80, null=True)),
                ('user_id', models.PositiveIntegerField(null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
    ]
