# Generated by Django 3.0 on 2020-02-19 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Svasth', '0002_auto_20200218_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('Event_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Event_Name', models.CharField(max_length=1000)),
                ('Event_Desc', models.TextField(max_length=1000)),
                ('Event_link', models.CharField(max_length=1000)),
                ('Event_img', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Doctors_Icon',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='Hospital_Logo',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='User_Icon',
            field=models.FileField(upload_to=''),
        ),
    ]
