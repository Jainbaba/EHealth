# Generated by Django 3.0.3 on 2020-02-21 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Svasth', '0009_auto_20200221_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Doctors_Specialisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Svasth.Specialisation'),
        ),
    ]