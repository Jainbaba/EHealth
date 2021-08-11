# Generated by Django 3.0.3 on 2020-02-21 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Svasth', '0008_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Doctors_Specialisation',
            field=models.CharField(choices=[(' Allergist', ' Allergist'), (' Anesthesiologist', ' Anesthesiologist'), (' Cardiologist', 'Cardiologist '), (' Orthopaedic', ' Orthopaedic'), (' Endocrinologist', ' Endocrinologist'), (' Dermatologist', ' Dermatologist')], max_length=254),
        ),
        migrations.CreateModel(
            name='Specialisation',
            fields=[
                ('Specialisation_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Specialisation_Name', models.CharField(max_length=1000)),
                ('Specialisation_Hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Svasth.Hospital')),
            ],
        ),
    ]
