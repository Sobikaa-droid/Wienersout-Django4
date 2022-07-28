# Generated by Django 4.0.6 on 2022-07-28 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('url', models.URLField(blank=True)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]