# Generated by Django 5.0.6 on 2024-08-28 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_buyerpay_payment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='status',
        ),
    ]
