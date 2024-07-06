# Generated by Django 5.0.6 on 2024-07-06 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0003_remove_profile_bio_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
