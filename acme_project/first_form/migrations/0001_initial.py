# Generated by Django 3.2.16 on 2024-03-13 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '0003_auto_20240313_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contingents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.contingents', verbose_name='Контингент/Возрастная группа')),
                ('name_of_diseases', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.nameofdiseases', verbose_name='Нозология')),
                ('territory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.territorialunit', verbose_name='Территория')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.units', verbose_name='Единица измерения')),
            ],
        ),
    ]
