# Generated by Django 3.2.7 on 2021-09-28 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap_grid_builder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gridcolpluginmodel',
            old_name='cols',
            new_name='cols_xs',
        ),
    ]