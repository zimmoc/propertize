# Generated by Django 4.2.11 on 2024-04-06 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0011_worker'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='used',
            field=models.BooleanField(default=False),
        ),
    ]