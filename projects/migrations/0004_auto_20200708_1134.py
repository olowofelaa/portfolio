# Generated by Django 3.0.8 on 2020-07-08 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200708_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.FilePathField(path='projects/static/img'),
        ),
    ]
