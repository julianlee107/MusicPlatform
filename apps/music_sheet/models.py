# _*_ coding=utf-8_*_

from datetime import datetime

from django.db import models

from users.models import UserProfile


# Create your models here.

class TypeDict(models.Model):
    type = models.Field(max_length=20,verbose_name="风格")
    desc = models.CharField(max_length=200,verbose_name="描述")
    add_time = models.DateField(default=datetime.now)

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name


class Music_sheet(models.Model):
    name = models.CharField(max_length=100,null=False,verbose_name="歌单名称")
    desc = models.TextField(verbose_name="歌曲描述")
    create_user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="创建用户")
    create_time = models.DateField(default=datetime.now,verbose_name="创建时间")
    sheet_type = models.ForeignKey(TypeDict, on_delete=models.CASCADE, verbose_name="歌单类型")
    fav_nums = models.IntegerField(default=0,verbose_name="收藏人数")
    listen_nums = models.IntegerField(default=0,verbose_name="播放次数")
    songs_nums = models.IntegerField(default=0,verbose_name="歌曲数")
    sheet_tags = models.CharField(max_length=50,verbose_name="歌单标签")
    sheet_image = models.ImageField(upload_to="music_sheets/%Y%m",verbose_name="歌单缩略图")

    class Meta:
        verbose_name = "歌单"
        verbose_name_plural = verbose_name


class Songs(models.Model):
    name = models.CharField(max_length=100,null=False,verbose_name="歌曲名")
    songs_detail = models.TextField(verbose_name="歌曲详情")
    songs_type = models.ForeignKey(TypeDict,on_delete=models.CASCADE,verbose_name="音乐类型")
    songs_resourse = models.URLField(verbose_name="播放链接")

    class Meta:
        verbose_name = "音乐"
        verbose_name_plural = verbose_name
