# Generated by Django 3.2.8 on 2022-06-09 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_universityprogram_thesis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universityprogram',
            name='notes',
            field=models.CharField(default='No', max_length=40, null=True, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='universityprogram',
            name='systemOfPayment',
            field=models.CharField(default='Per year', max_length=40, null=True, verbose_name='System of Payment'),
        ),
        migrations.AlterField(
            model_name='universityprogram',
            name='taksitFees',
            field=models.CharField(default='', max_length=40, null=True, verbose_name='Taksit Fees'),
        ),
        migrations.AlterField(
            model_name='universityprogram',
            name='thesis',
            field=models.CharField(default='No', max_length=40, null=True, verbose_name='Thesis'),
        ),
    ]
