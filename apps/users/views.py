
from datetime import datetime

from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.hashers import make_password # 对密码进行加密
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import login,logout,authenticate #登录和验证模块
from django.views import View
from .models import UserProfile
# Create your views here.

class UserForm(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control rounded input-lg text-center no-border',
                                                                              'placeholder':'Username'}))
    email = forms.EmailField(label='',required=False,widget=forms.TextInput(attrs={'class':'form-control rounded input-lg text-center no-border',
                                                                                'placeholder':'Email'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control rounded input-lg text-center no-border',
                                                                            'placeholder':'Password'}))

class CustomBackend(ModelBackend):
    """自定义邮箱与账户登录认证"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None




class LogInView(View):
    """登录功能"""
    def get(self,request):
        # get请求直接返回页面
        userform = UserForm
        return render(request,"login.html",{'userform':userform})

    def post(self,request):
        userform = UserForm(request.POST)
        if userform.is_valid():
            # 输入通过UserForm验证
            # 取用户输入值
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = authenticate(username=username,password=password)
            if user is not None:
                # 数据库匹配
                # username可能是用户名也可能是email
                try:
                    user = UserProfile.objects.get(Q(username=username))
                except:
                    user = UserProfile.objects.get(Q(email=username))
                user.last_login = datetime.now()
                response = HttpResponseRedirect('/index/')
                response.set_cookie("cookie_username",user.username,3600)
                login(request,user)
                return response
                # return render(request,'index.html',{"username":user.username})
            else:
                # 账号密码错误，数据库匹配不上
                return render(request,'login.html',{"userform":userform,"msg":"账号或密码错误"})
        else:
            # 没通过UserForm的验证，返回错误给前端
            return render(request,'login.html',{'userform':userform})


class RegisterView(View):
    def get(self,request):
        userform = UserForm()
        return render(request,'register.html',{'userform':userform})

    def post(self,request):
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            email = userform.cleaned_data['email']
            if UserProfile.objects.filter(username=username)|UserProfile.objects.filter(email=email):
                return render(request,'register.html',{'userform':userform,'msg':'用户已经注册'})
            password = userform.cleaned_data['password']
            user_profile = UserProfile()
            user_profile.username = username
            user_profile.email = email
            user_profile.password = make_password(password)
            user_profile.save()
            return HttpResponseRedirect('/login/')
            # return render(request,"login.html",{'userform':userform})
        else:
            return render(request,'register.html',{"userform":userform})


def get_index(request):
    # 验证是否登录
    if request.user.is_authenticated:
        username = request.COOKIES.get('cookie_username')
        return render(request, "index.html",{'username':username})
        # return render(request,'index.html')
    else:
        return HttpResponseRedirect('/login/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def profile(request):
    return render(request,"profile.html")