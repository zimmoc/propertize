# Generated by Django 4.2.11 on 2024-03-30 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0006_tenant_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='apartment',
            field=models.CharField(default=0, max_length=50),
        ),
    ]