# Generated by Django 3.2.16 on 2023-02-17 16:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0017_remove_delivery_measurements'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='measurements',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
