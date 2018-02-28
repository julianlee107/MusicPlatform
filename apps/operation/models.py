#_*_ encoding:utf-8_*_
from datetime import datetime

from django.db import models
from music_sheet.models import Music_sheet

from users.models import UserProfile


# Create your models here.


class MusicSheetComments(models.Model):
    #歌单评论
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="用户")
    music_sheet = models.ForeignKey(Music_sheet,on_delete=models.CASCADE,verbose_name="歌单")
    comments = models.CharField(max_length=200,verbose_name="评论")
    add_time = models.DateField(default=datetime.now,verbose_name="评论时间")

    class Meta:
        verbose_name = "歌单评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    #用户收藏
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="用户")
    fav_id = models.IntegerField(default=0,verbose_name="数据ID")
    fav_type= models.IntegerField(choices=((1,"歌单"),(2,"歌曲"),(3,"歌手")),default=1,verbose_name="收藏类型")
    add_time = models.DateField(default=datetime.now,verbose_name="收藏时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0,verbose_name="接受用户ID")  # 0为全员，非0为用户ID
    message = models.CharField(max_length=500,verbose_name="消息类容")
    has_read = models.BooleanField(default=False,verbose_name="是否已读")
    add_time = models.DateField(default=datetime.now,verbose_name="发送时间")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name


class UserMusicSheet(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="用户")
    music_sheet = models.ForeignKey(Music_sheet,on_delete=models.CASCADE,verbose_name="歌单")
    add_time = models.DateField(default=datetime.now, verbose_name="创建时间")

    class Meta:
        verbose_name = "用户歌单"
        verbose_name_plural = verbose_name
