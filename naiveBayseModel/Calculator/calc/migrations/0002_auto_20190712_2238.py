# Generated by Django 2.2.3 on 2019-07-12 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hypotese',
            new_name='Hypoteses',
        ),
        migrations.RenameField(
            model_name='hypoteses',
            old_name='nome',
            new_name='name',
        ),
    ]
