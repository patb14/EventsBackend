# Generated by Django 4.2.1 on 2023-06-05 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_delete_eventtime_session_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='current_occupancy',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='session',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
