"""MusicPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from users.views import get_index,LogInView,RegisterView,logout_view,ActiveUserView,ProfileView,ChangeProfileView
from music_sheet.views import MusicSheetView,SongsView
from django.conf.urls import url
import xadmin
xadmin.autodiscover()


urlpatterns = [
    url('xadmin/', xadmin.site.urls),
    # url('admin/', admin.site.urls),
    url('index/$',get_index),
    url('register/$',RegisterView.as_view(),name='注册'),
    url('profile/(?P<username>.*)/$',ProfileView.as_view(), name='用户页面'),
    url('login/$',LogInView.as_view(),name='登录'),
    url('logout/$',logout_view),
    url('active/(?P<active_code>.*)/$',ActiveUserView.as_view(),name='用户激活'), # 配置激活账户的链接
    url('changeprofile/$',ChangeProfileView.as_view(),name='信息修改'),
    url('listen/$',MusicSheetView.as_view(),name='歌单页面'),
    url('songs/$',SongsView.as_view(),name='歌曲页面'),
    url('',get_index)
]
