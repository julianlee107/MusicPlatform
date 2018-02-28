# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-28 10:49
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music_sheet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicSheetComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=200, verbose_name='评论')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='评论时间')),
                ('music_sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_sheet.Music_sheet', verbose_name='歌单')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '歌单评论',
                'verbose_name_plural': '歌单评论',
            },
        ),
        migrations.CreateModel(
            name='UserFavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_id', models.IntegerField(default=0, verbose_name='数据ID')),
                ('fav_type', models.IntegerField(choices=[(1, '歌单'), (2, '歌曲'), (3, '歌手')], default=1, verbose_name='收藏类型')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='收藏时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户收藏',
                'verbose_name_plural': '用户收藏',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0, verbose_name='接受用户ID')),
                ('message', models.CharField(max_length=500, verbose_name='消息类容')),
                ('has_read', models.BooleanField(default=False, verbose_name='是否已读')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='发送时间')),
            ],
            options={
                'verbose_name': '用户消息',
                'verbose_name_plural': '用户消息',
            },
        ),
        migrations.CreateModel(
            name='UserMusicSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('music_sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_sheet.Music_sheet', verbose_name='歌单')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户歌单',
                'verbose_name_plural': '用户歌单',
            },
        ),
    ]
