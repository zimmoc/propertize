# Generated by Django 4.2.11 on 2024-03-27 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0011_invitationcode_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitationcode',
            name='name',
        ),
        migrations.AddField(
            model_name='invitationcode',
            name='tenant_name',
            field=models.CharField(default='Jane Doe', max_length=70),
        ),
    ]
