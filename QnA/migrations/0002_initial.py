# Generated by Django 4.1.2 on 2022-10-27 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('QnA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='hashtags',
            field=models.ManyToManyField(blank=True, to='main.hashtag'),
        ),
        migrations.AddField(
            model_name='answer',
            name='a_parent_comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='QnA.answer'),
        ),
        migrations.AddField(
            model_name='answer',
            name='qna_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='QnA.question'),
        ),
    ]
