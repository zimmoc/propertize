# Generated by Django 4.2.11 on 2024-04-03 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0009_alter_maintenancerequest_scheduled_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancerequest',
            name='contractor_note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='maintenancerequest',
            name='description',
            field=models.TextField(),
        ),
    ]