# Generated by Django 3.0.3 on 2020-03-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Svasth', '0011_auto_20200302_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='User_Password',
            field=models.CharField(max_length=255),
        ),
    ]
