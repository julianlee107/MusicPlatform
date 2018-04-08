import xadmin

from .models import TypeDict,Music_sheet,Songs,Singer

# Register your models here.

class TypeDictAdmin(object):
    list_display = ['type','desc','add_time']
    search_fields = ['type','desc','add_time']
    list_filter = ['type','desc','add_time']


class MusicSheetAdmin(object):
    list_display = ['id','name','desc','create_user','create_time',
                    'sheet_type','fav_nums','sheet_tags','sheet_image']
    search_fields = ['id','name','desc','create_user','create_time',
                    'sheet_type','fav_nums','sheet_tags','sheet_image']
    list_filter = ['id','name','desc','create_user','create_time',
                    'sheet_type','fav_nums','sheet_tags','sheet_image']
    style_fields = {'songs': 'm2m_transfer'}    #复选框



class SongsAdmin(object):
    list_display = ['id','name','singer_name','song_detail','song_type','song_resourse']
    search_fields = ['id','name','singer_name','song_detail','song_type','song_resourse']
    list_filter = ['id','name','singer_name','song_detail','song_type','song_resourse']


class SingerAdmin(object):
    list_display = ['id','name','fav_nums','singer_brief','add_time']
    search_fields = ['id','name','fav_nums','singer_brief','add_time']
    list_filter = ['id','name','fav_nums','singer_brief','add_time']

xadmin.site.register(TypeDict,TypeDictAdmin)
xadmin.site.register(Music_sheet,MusicSheetAdmin)
xadmin.site.register(Songs,SongsAdmin)
xadmin.site.register(Singer,SingerAdmin)