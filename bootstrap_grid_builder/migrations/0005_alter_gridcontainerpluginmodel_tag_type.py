# Generated by Django 3.2.7 on 2021-09-28 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootstrap_grid_builder', '0004_auto_20210928_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gridcontainerpluginmodel',
            name='tag_type',
            field=models.CharField(blank=True, choices=[('section', 'Section'), ('div', 'Div')], default='div', max_length=64, verbose_name='Tag Type'),
        ),
    ]
