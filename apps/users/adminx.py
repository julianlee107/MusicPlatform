from django.contrib import admin

# Register your models here.

import xadmin
from xadmin import views

from .models import UserProfile
from .models import EmailVerifyRecord

class GlobalSettion(object):
    site_title = "JMusic"
    menu_style = 'accordion'


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class UserProfileAdmin(object):
    list_display = ['id','username','gender','mobile','image']
    search_fileds = ['id','username','gender','mobile','address']
    list_fileter = ['id','username','gender','mobile','address']


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']

xadmin.site.register(views.CommAdminView,GlobalSettion)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
