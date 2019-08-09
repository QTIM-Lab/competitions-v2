# Generated by Django 2.1.2 on 2019-07-29 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0040_remove_submission_ignore_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitionparticipant',
            name='chahub_data_hash',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='competitionparticipant',
            name='chahub_needs_retry',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='competitionparticipant',
            name='chahub_timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]