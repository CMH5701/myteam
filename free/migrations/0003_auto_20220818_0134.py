# Generated by Django 3.2.13 on 2022-08-17 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('free', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='free',
            old_name='nickname',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='free_clip',
            old_name='nickname',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='free_like',
            old_name='nickname',
            new_name='user',
        ),
    ]
