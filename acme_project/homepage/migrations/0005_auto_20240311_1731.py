# Generated by Django 3.2.16 on 2024-03-11 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20240311_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='territorialunit',
            old_name='district_id',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='territorialunit',
            old_name='geo_category_id',
            new_name='geo_category',
        ),
    ]
