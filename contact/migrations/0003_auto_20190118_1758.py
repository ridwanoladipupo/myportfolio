# Generated by Django 2.1.4 on 2019-01-18 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_delete_consult'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='contact',
            name='fname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='lname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
