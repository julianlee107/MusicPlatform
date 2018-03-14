

# Register your models here.
import xadmin
from .models import MusicSheetComments,UserMessage,UserMusicSheet,UserFavorite

class MusicSheetCommentsAdmin(object):
    list_display = ['user','music_sheet','comments','add_time']
    search_fields = ['user','music_sheet','comments','add_time']
    list_filter = ['user','music_sheet','comments','add_time']


class UserFavoriteAdmin(object):
    list_display = ['user','fav_id','fav_type','add_time']
    search_fields = ['user','fav_id','fav_type','add_time']
    list_filter = ['user','fav_id','fav_type','add_time']


class UserMessageAdmin(object):
    list_display = ['user','message','has_read','add_time']
    search_fields = ['user','message','has_read','add_time']
    list_filter = ['user','message','has_read','add_time']


class UserMusicSheetAdmin(object):
    list_display = ['user','music_sheet','add_time']
    search_fields = ['user','music_sheet','add_time']
    list_filter = ['user','music_sheet','add_time']


xadmin.site.register(MusicSheetComments,MusicSheetCommentsAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserMusicSheet,UserMusicSheetAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
