# Generated by Django 3.2.16 on 2023-03-04 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothe', '0002_alter_clothe_cloth_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothe',
            name='cloth_thumbnail',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
    ]