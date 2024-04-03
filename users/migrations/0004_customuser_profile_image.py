# Generated by Django 4.2.11 on 2024-04-02 21:54

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_assigned_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
