# Generated by Django 4.0.6 on 2022-07-28 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_description_alter_blog_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(max_length=140),
        ),
    ]
