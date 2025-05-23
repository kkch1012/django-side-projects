# Generated by Django 4.2.20 on 2025-04-24 03:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_link_posts_user_like_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following_relationships', to=settings.AUTH_USER_MODEL, verbose_name='팔로우를 요청한 사용자')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_relationships', to=settings.AUTH_USER_MODEL, verbose_name='팔로우 요청의 대상')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='followers', through='users.Relationship', to=settings.AUTH_USER_MODEL, verbose_name='팔로우 중인 사용자들'),
        ),
    ]
