# _*_ coding=utf-8 _*_
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

from datetime import datetime


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length = 16,verbose_name = "昵称",default="")
    birthday = models.DateField(verbose_name="生日",null=True)
    gender = models.CharField(choices=(("male","男"),("female","女")),default="male",max_length=6,verbose_name="性别")
    address = models.CharField(max_length=100,default="",verbose_name='地址')
    mobile = models.CharField(max_length=11,null=True,blank=True,verbose_name='联系方式')
    image = models.ImageField(upload_to="image/%Y/%m",default="image/default.png",max_length=100,verbose_name='头像')
    info = models.TextField(default='', verbose_name='个人信息')
    about_me = models.CharField(max_length=100, default='this person is very lazy', verbose_name='关于')
    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name


class EmailVerifyRecord(models.Model):
    email_choices = (
        ('register', '注册'),
        ('forget', '找回密码'),
    )
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=email_choices, max_length=10, verbose_name=u'验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'发送时间')

    class Meta:
        verbose_name = '邮箱验证'
        verbose_name_plural = verbose_name