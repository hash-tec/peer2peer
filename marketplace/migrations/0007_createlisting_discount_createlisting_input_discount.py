# Generated by Django 5.0.6 on 2024-08-12 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0006_alter_requestitem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='createlisting',
            name='discount',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='createlisting',
            name='input_discount',
            field=models.DecimalField(decimal_places=0, max_digits=10, null=True),
        ),
    ]
