# Generated by Django 3.2.13 on 2022-08-19 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_alter_review_r_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='r_clips',
            new_name='r_clicks',
        ),
    ]