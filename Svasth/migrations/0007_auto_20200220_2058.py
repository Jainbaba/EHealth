# Generated by Django 3.0 on 2020-02-20 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Svasth', '0006_logintime_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='User_BirthDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='User_BloodGroup',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='User_Icon',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]