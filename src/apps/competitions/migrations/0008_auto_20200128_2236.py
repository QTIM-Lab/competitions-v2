# Generated by Django 2.2.9 on 2020-01-28 22:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competitions', '0007_merge_20200125_0032'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='competitionparticipant',
            unique_together={('user', 'competition')},
        ),
    ]
