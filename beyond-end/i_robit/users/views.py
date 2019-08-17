from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm
import json

from .forms import LoginForm
# Create your views here.

def login_view(request):
    '''登录视图'''
    if request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():#验证是否符合表单的要求
            username = request.POST.get('username')
            passsword = request.POST.get('password')
            user = authenticate(username=username,passsword=passsword)
            
            if user:#验证用户名密码是否匹配
                login(request,user)
                match = True
            else:
                match = False
            #前端要求的数据：用户名、密码、是否匹配
            context = {'match':match}
            return JsonResponse(context) 
        else:
            pass
    else:   #不是POST请求就返回一个空表单
        context = {'match':False}
        return JsonResponse(context)

def logout_view(request):
    '''注销视图'''
    logout(request)
    context = {'status':'exit'}
    return JsonResponse(context)

def register_view(request):
    '''注册视图'''
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():  #表单验证
            new_user = form.save()
            username = new_user.username
            password = request.POST['password1']
            authenticated_user = authenticate(username=username,
            password=password)
            if authenticated_user is not None:
                login(request,authenticated_user)
                context = {'status':True}
                return JsonResponse(context)
    context = {'status':False}
    return JsonResponse(context)




