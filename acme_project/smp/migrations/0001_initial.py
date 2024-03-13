# Generated by Django 3.2.16 on 2024-03-13 10:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Средний многолетний показатель')),
                ('from_to_year', models.CharField(max_length=10, verbose_name='Период расчета (пример: 2010_2022)')),
                ('from_year', models.DateField(verbose_name='Начальная дата')),
                ('to_year', models.DateField(verbose_name='Конечная дата')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='smp_form', to='homepage.statform', verbose_name='Номер формы')),
                ('name_of_diseases', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='smp_nod', to='homepage.nameofdiseases', verbose_name='Нозология')),
                ('territorial_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='smp_territorial_unit', to='homepage.territorialunit', verbose_name='Регион')),
            ],
            options={
                'verbose_name': 'СМП',
                'verbose_name_plural': 'СМП',
            },
        ),
    ]
