# Generated by Django 3.2.16 on 2023-02-17 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0011_alter_delivery_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='address',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='delivered',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='email',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='measurements',
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='phone',
        ),
    ]
