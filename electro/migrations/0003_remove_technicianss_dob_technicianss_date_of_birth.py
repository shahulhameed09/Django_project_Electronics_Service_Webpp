# Generated by Django 4.0.4 on 2022-08-24 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electro', '0002_alter_technicianss_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technicianss',
            name='DOB',
        ),
        migrations.AddField(
            model_name='technicianss',
            name='Date_Of_Birth',
            field=models.CharField(default='', max_length=10),
        ),
    ]