# Generated by Django 3.1 on 2020-09-01 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0011_listname_body'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='filmlist',
            unique_together={('list', 'film')},
        ),
    ]