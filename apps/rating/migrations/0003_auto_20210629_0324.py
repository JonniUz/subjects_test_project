# Generated by Django 3.1.5 on 2021-06-28 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0002_auto_20210628_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=2550),
        ),
    ]
