# Generated by Django 4.2.11 on 2024-04-06 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0025_remove_property_contractors_and_more'),
        ('maintenance', '0010_alter_maintenancerequest_contractor_note_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('code_name', models.CharField(max_length=120)),
                ('contractor', models.BooleanField(default=True)),
                ('code', models.CharField(blank=True, max_length=5, unique=True)),
                ('assigned_properties', models.ManyToManyField(related_name='assigned_properties', to='properties.property')),
            ],
        ),
    ]
