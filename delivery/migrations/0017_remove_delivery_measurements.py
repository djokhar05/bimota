# Generated by Django 3.2.16 on 2023-02-17 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0016_delivery_measurements'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='measurements',
        ),
    ]
