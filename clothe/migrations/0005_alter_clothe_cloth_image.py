# Generated by Django 3.2.16 on 2023-03-04 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothe', '0004_alter_clothe_cloth_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothe',
            name='cloth_image',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
    ]