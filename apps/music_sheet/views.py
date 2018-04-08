from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from users.models import UserProfile
from .models import Songs,Singer,Music_sheet,TypeDict
# Create your views here.


class MusicSheetView(View):
    def get(self,request):
        username = request.COOKIES.get('cookie_username')
        user = UserProfile.objects.get(username=username)
        all_music_sheet = Music_sheet.objects.all()
        type_id = request.GET.get("type","")
        if type_id:
            all_music_sheet = Music_sheet.objects.filter(sheet_type_id=int(type_id))
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_music_sheet, 12, request=request)
        all_music_sheet = p.page(page)
        # 显示类型
        typelist = TypeDict.objects.all()

        return render(request,'musiclist.html',{'username':username,
                                                'user':user,
                                                'typelist':typelist,
                                                'music_sheets':all_music_sheet})


class SongsView(View):

    def get(self,request):

        username = request.COOKIES.get('cookie_username')
        if username is not None:
            user = UserProfile.objects.get(username=username)
            typelist = TypeDict.objects.all()
            song_detail = Songs()
            songs = Songs.objects.all()
            #筛选类别
            type_id = request.GET.get("type","")
            if type_id:
                songs = Songs.objects.filter(song_type_id=int(type_id))
            #分页
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(songs, 10,request=request)

            songs = p.page(page)
            return render(request,'songs.html',{'username':username,'user':user,'songs':songs,'typelist':typelist,'song_detail':song_detail})
        else:
            return HttpResponseRedirect('/login/')