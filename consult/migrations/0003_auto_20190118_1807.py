# Generated by Django 2.1.4 on 2019-01-18 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0002_auto_20190118_1758'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consult',
            old_name='fname',
            new_name='name',
        ),
    ]
