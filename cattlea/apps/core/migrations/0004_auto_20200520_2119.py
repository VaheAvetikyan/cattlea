# Generated by Django 3.0.6 on 2020-05-20 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200515_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoe',
            name='sex',
        ),
        migrations.AddField(
            model_name='product',
            name='sex',
            field=models.CharField(choices=[('M', 'male'), ('F', 'female')], default='M', max_length=2),
        ),
    ]
