# Generated by Django 5.0.6 on 2024-08-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0011_alter_createlisting_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createlisting',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
    ]
