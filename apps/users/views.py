
from datetime import datetime,time

from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect,HttpResponse
from django.db.models import Q
from django.contrib.auth.hashers import make_password # 对密码进行加密
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import login,logout,authenticate #登录和验证模块
from django.views import View
from .models import UserProfile,EmailVerifyRecord
from .utils.emails_send import send_register_email
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
    """注册"""
    def get(self,request):
        userform = UserForm
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
            user_profile.is_active = False # 设置注册账户没有激活
            user_profile.password = make_password(password)
            user_profile.save()

            send_register_email(user_profile.email,'register') #用邮箱验证激活
            return HttpResponseRedirect('/login/')
            # return render(request,"login.html",{'userform':userform})
        else:
            return render(request,'register.html',{"userform":userform})


class  ActiveUserView(View):
    """账号激活"""
    def get(self,request,active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request,'register.html',{'msg':'激活失败'})
        return HttpResponseRedirect('/login/')


def get_index(request):
    # 验证是否登录
    if request.user.is_authenticated:
        username = request.COOKIES.get('cookie_username')
        user = UserProfile.objects.get(username=username)
        return render(request, "index.html",{'username':username,'user':user})
        # return render(request,'index.html')
    else:
        return HttpResponseRedirect('/login/')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def profile(request,username):
    if request.user.is_authenticated:
        # return HttpResponseRedirect('/profile/?'+request.GET('username'))
        return render(request, 'profile.html', {'username': username})
    # return render(request,"profile.html")


class ProfileView(View):
    def get(self,request,username):
        if request.user.is_authenticated:
            user = UserProfile.objects.get(username=username)
            return render(request,'profile.html', {'username': username, 'user': user})
        else:
            return HttpResponseRedirect('/login/')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['username','first_name','last_name','email',
                  'gender','birthday','address','mobile','image','about_me','info']
        labels = {
            'image':'Profile Picture'
        }


class ChangeProfileView(View):
    def get(self,request):
        if request.user.is_authenticated:

            username = request.COOKIES.get('cookie_username')
            old_userprofile = UserProfile.objects.get(username=username)
            user_profile = UserProfileForm(instance=old_userprofile)

            # user_profile.username = old_userprofile.username
            # user_profile.last_name = old_userprofile.last_name
            # user_profile.first_name = old_userprofile.first_name
            # user_profile.email = old_userprofile.email
            # user_profile.gender = old_userprofile.gender
            # user_profile.address = old_userprofile.address
            # user_profile.image = old_userprofile.image
            # user_profile.about_me = old_userprofile.about_me
            # user_profile.info = old_userprofile.info
            return render(request,'change-profile.html',{'userprofile':user_profile,'username':username})
        else:
            return HttpResponseRedirect('/login/')
    def post(self,request):
        user_profile = UserProfileForm(request.POST)
        username = request.COOKIES.get('cookie_username')
        changed_userporfile = UserProfile.objects.get(username=username)
        changed_userporfile.username = request.POST.get('username','')
        changed_userporfile.first_name = request.POST.get('first_name','')
        changed_userporfile.last_name = request.POST.get('last_name','')
        changed_userporfile.email = request.POST.get('email','')
        changed_userporfile.gender = request.POST.get('gender','')
        changed_userporfile.address = request.POST.get('address','')
        changed_userporfile.image = request.POST.get('image','')
        changed_userporfile.info = request.POST.get('info','')
        changed_userporfile.about_me = request.POST.get('about_me','')
        changed_userporfile.mobile = request.POST.get('mobile','')
        changed_userporfile.birthday = datetime.strptime(request.POST.get('birthday'),"%Y/%m/%d")
        changed_userporfile.save()
        response = HttpResponseRedirect('/index/')
        response.set_cookie("cookie_username",changed_userporfile.username,3600)
        return response



