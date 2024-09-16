# Generated by Django 5.1 on 2024-08-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GovChat_core', '0036_alter_user_business_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='ingest_error',
            field=models.TextField(blank=True, help_text='error, if any, encountered during ingest', max_length=2048, null=True),
        ),
    ]
