# Generated by Django 5.0.6 on 2024-08-14 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0010_seller_createlisting_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createlisting',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=100, null=True),
        ),
    ]
