# Generated by Django 4.0.4 on 2022-11-04 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electro', '0015_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='profile_pics'),
        ),
    ]