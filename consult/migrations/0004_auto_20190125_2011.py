# Generated by Django 2.1.4 on 2019-01-25 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0003_auto_20190118_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consult',
            name='categories',
            field=models.CharField(choices=[('GR', 'Graphics Design'), ('MR', 'Mentorship'), ('ST', 'System Troubleshooting'), ('WD', 'Web Development')], default='GR', max_length=2),
        ),
        migrations.AlterField(
            model_name='consult',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]