# Generated by Django 3.1 on 2020-08-12 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_film_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='genre',
            new_name='genres',
        ),
    ]