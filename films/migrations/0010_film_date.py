# Generated by Django 3.1 on 2020-08-27 08:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0009_auto_20200827_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
