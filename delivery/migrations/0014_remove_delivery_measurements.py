# Generated by Django 3.2.16 on 2023-02-17 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0013_auto_20230217_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='measurements',
        ),
    ]
