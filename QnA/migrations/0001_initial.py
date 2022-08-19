# Generated by Django 3.2.13 on 2022-08-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=50)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('a_photo', models.ImageField(blank=True, null=True, upload_to='a_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('q_date', models.DateTimeField(verbose_name='data published')),
                ('q_photo', models.ImageField(blank=True, null=True, upload_to='q_images/')),
                ('q_clips', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('q_likes', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]