# Generated by Django 4.2.11 on 2024-05-03 10:08
from django.db import migrations, models
from storages.backends import s3boto3


class Migration(migrations.Migration):
    dependencies = [
        ("GovChat_core", "0003_chathistory_file_chatmessage_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file",
            name="original_file",
            field=models.FileField(storage=s3boto3.S3Boto3Storage, upload_to=""),
        ),
        migrations.AddField(
            model_name="file",
            name="original_file_name",
            field=models.TextField(blank=True, max_length=2048, null=True),
        ),
    ]
