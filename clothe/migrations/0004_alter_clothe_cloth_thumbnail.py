# Generated by Django 3.2.16 on 2023-03-04 09:22

from django.db import migrations
import thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clothe', '0003_clothe_cloth_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothe',
            name='cloth_thumbnail',
            field=thumbnails.fields.ImageField(default='default.jpg', upload_to='images'),
        ),
    ]
