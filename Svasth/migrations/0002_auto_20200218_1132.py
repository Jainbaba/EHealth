# Generated by Django 3.0 on 2020-02-18 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Svasth', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Doctors',
            new_name='Doctor',
        ),
        migrations.AlterField(
            model_name='hospital',
            name='Hospital_Contact',
            field=models.CharField(max_length=15),
        ),
    ]
