# Generated by Django 4.2.5 on 2023-09-25 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_mytodods_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytodods',
            name='img',
            field=models.ImageField(upload_to='todoimg'),
        ),
    ]