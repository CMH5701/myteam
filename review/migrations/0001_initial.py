# Generated by Django 3.2.13 on 2022-08-17 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_title', models.CharField(max_length=200)),
                ('r_body', models.TextField()),
                ('r_location', models.CharField(blank=True, max_length=20, null=True)),
                ('r_photo', models.ImageField(blank=True, upload_to='images/')),
                ('r_receipt', models.ImageField(blank=True, upload_to='images/')),
                ('r_nickname', models.CharField(blank=True, max_length=20, null=True)),
                ('r_clips', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('r_date', models.DateTimeField(verbose_name='data published')),
                ('r_likes', models.CharField(blank=True, max_length=20, null=True)),
                ('hashtags', models.ManyToManyField(blank=True, to='main.Hashtag')),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='account.profile')),
                ('r_clip', models.ManyToManyField(blank=True, related_name='r_clip', to='account.Profile')),
                ('r_like', models.ManyToManyField(blank=True, related_name='r_likes', to='account.Profile')),
                ('r_user', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r_user', to='account.profile')),
            ],
        ),
        migrations.CreateModel(
            name='r_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='account.profile')),
                ('r_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review.review')),
                ('r_parent_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='review.r_comment')),
            ],
        ),
    ]