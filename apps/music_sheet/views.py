from django.shortcuts import render
from django.views import View
# Create your views here.


class MusicSheetView(View):
    def get(self,request):
        username = request.COOKIES.get('cookie_username')
        return render(request,'musiclist.html',{'username':username})


class SongsView(View):
    def get(self,request):
        username = request.COOKIES.get('cookie_username')
        return render(request,'songs.html',{'username':username})