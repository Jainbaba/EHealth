# Generated by Django 3.0 on 2020-02-19 04:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Svasth', '0004_event_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Event_Date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
