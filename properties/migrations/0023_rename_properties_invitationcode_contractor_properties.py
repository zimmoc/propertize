# Generated by Django 4.2.11 on 2024-04-06 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0022_invitationcode_properties'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invitationcode',
            old_name='properties',
            new_name='contractor_properties',
        ),
    ]
