# Generated by Django 4.2.11 on 2024-03-27 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0002_tenant_outstanding_rent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tenant',
            old_name='renter',
            new_name='resident',
        ),
    ]
