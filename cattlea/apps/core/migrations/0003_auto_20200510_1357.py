# Generated by Django 3.0.6 on 2020-05-10 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200510_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='available_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='available_hy',
        ),
    ]
