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
    ]

    operations = [
        migrations.CreateModel(
            name='Music_sheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='歌单名称')),
                ('desc', models.TextField(verbose_name='歌曲描述')),
                ('create_time', models.DateField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('listen_nums', models.IntegerField(default=0, verbose_name='播放次数')),
                ('songs_nums', models.IntegerField(default=0, verbose_name='歌曲数')),
                ('sheet_tags', models.CharField(max_length=50, verbose_name='歌单标签')),
                ('sheet_image', models.ImageField(upload_to='music_sheets/%Y%m', verbose_name='歌单缩略图')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建用户')),
            ],
            options={
                'verbose_name': '歌单',
                'verbose_name_plural': '歌单',
            },
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='歌曲名')),
                ('songs_detail', models.TextField(verbose_name='歌曲详情')),
                ('songs_resourse', models.URLField(verbose_name='播放链接')),
            ],
            options={
                'verbose_name': '音乐',
                'verbose_name_plural': '音乐',
            },
        ),
        migrations.CreateModel(
            name='TypeDict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.Field(max_length=20, verbose_name='风格')),
                ('desc', models.CharField(max_length=200, verbose_name='描述')),
                ('add_time', models.DateField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '类别',
                'verbose_name_plural': '类别',
            },
        ),
        migrations.AddField(
            model_name='songs',
            name='songs_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_sheet.TypeDict', verbose_name='音乐类型'),
        ),
        migrations.AddField(
            model_name='music_sheet',
            name='sheet_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_sheet.TypeDict', verbose_name='歌单类型'),
        ),
    ]