# Generated by Django 4.2.11 on 2024-04-05 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0018_property_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitationcode',
            name='tenant_name',
            field=models.CharField(default='Jane Doe', max_length=70, verbose_name='Tenant'),
        ),
    ]