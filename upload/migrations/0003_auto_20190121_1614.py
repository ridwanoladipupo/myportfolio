# Generated by Django 2.1.4 on 2019-01-21 15:14

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20190121_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='screenshot',
            field=pyuploadcare.dj.models.ImageField(),
        ),
    ]
