# Generated by Django 5.0.6 on 2024-08-28 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_payment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='status',
        ),
    ]
