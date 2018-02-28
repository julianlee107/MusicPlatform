# _*_ coding=utf-8 _*_
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length = 16,verbose_name = "昵称",default="")
    birthday = models.DateField(verbose_name="生日",null=True)
    gender = models.CharField(choices=(("male","男"),("female","女")),default="female",max_length=5,verbose_name="性别")
    address = models.CharField(max_length=100,default="")
    mobile = models.CharField(max_length=11,null=True,blank=True)
    image = models.ImageField(upload_to="image/%Y/%m",default="image/default.png",max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name