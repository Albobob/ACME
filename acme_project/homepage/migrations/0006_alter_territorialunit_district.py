# Generated by Django 3.2.16 on 2024-03-11 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_auto_20240311_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='territorialunit',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district', to='homepage.districtname'),
        ),
    ]
