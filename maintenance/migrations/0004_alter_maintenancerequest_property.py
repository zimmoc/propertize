# Generated by Django 4.2.11 on 2024-03-28 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0013_alter_invitationcode_tenant_name'),
        ('maintenance', '0003_alter_maintenancerequest_contractor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancerequest',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_property', to='properties.property'),
        ),
    ]
