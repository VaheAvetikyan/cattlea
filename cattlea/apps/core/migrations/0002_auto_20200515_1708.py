# Generated by Django 3.0.6 on 2020-05-15 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=32)),
                ('color_en', models.CharField(max_length=32, null=True)),
                ('color_hy', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='color_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color_hy',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(related_name='colors', to='core.Color'),
        ),
    ]