# Generated by Django 3.2.8 on 2022-06-09 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20220609_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universityprogram',
            name='thesis',
            field=models.CharField(default='No', max_length=40, verbose_name='Thesis'),
        ),
    ]
