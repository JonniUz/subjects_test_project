# Generated by Django 3.1.5 on 2021-06-28 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Fanlar'},
        ),
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name_plural': 'Javoblar'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name_plural': 'Savollar'},
        ),
    ]
