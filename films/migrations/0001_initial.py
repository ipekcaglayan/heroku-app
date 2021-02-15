# Generated by Django 3.1 on 2020-08-11 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tconst', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('minutes', models.CharField(max_length=200)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.genre')),
            ],
        ),
    ]