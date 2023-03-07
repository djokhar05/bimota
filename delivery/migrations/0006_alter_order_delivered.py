# Generated by Django 3.2.16 on 2023-02-15 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_auto_20230215_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered',
            field=models.CharField(choices=[('false', 'Not Delivered'), ('true', 'Delivered')], default='false', max_length=200),
        ),
    ]