# Generated by Django 4.2.11 on 2024-04-01 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0015_alter_propertynotice_posted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertynotice',
            name='important',
            field=models.BooleanField(default=False),
        ),
    ]
