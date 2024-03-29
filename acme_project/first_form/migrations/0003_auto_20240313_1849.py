# Generated by Django 3.2.16 on 2024-03-13 15:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20240313_1831'),
        ('first_form', '0002_auto_20240313_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstform',
            name='period_month',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.periodmonth', verbose_name='Месяц'),
        ),
        migrations.AddField(
            model_name='firstform',
            name='period_year',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.periodyear', verbose_name='Год'),
        ),
        migrations.AlterField(
            model_name='firstform',
            name='value',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Значение'),
        ),
    ]
