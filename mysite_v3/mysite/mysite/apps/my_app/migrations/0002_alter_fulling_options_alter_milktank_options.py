# Generated by Django 4.0.3 on 2022-03-12 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fulling',
            options={'verbose_name': 'Заливки'},
        ),
        migrations.AlterModelOptions(
            name='milktank',
            options={'verbose_name': 'Цистерна', 'verbose_name_plural': 'Цистерны'},
        ),
    ]