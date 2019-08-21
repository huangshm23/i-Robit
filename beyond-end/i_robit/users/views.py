from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
import json
from .models import User

# Create your views here.

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    '''登录视图'''
    #match:0-匹配成功;1-账号不存在;2-密码错误
    context = {}
    if request.method == 'POST':
        username = request.POST.get('params[account]')
        password = request.POST.get('params[password]')
        count = User.objects.filter(username=username).count()
        user = User.objects.get(username=username)
        if count == 0:
            context = {'status':1}
        else:
            if password == user.password:
                context = {'status':0}
            else:
                context = {'status':2}
    return JsonResponse(context)

@csrf_exempt
def logout_view(request):
    '''注销视图'''
    logout(request)
    context = {'status':0}
    return JsonResponse(context)

@csrf_exempt
def register_view(request):
    '''注册视图:status=0表示成功,status=1表示账号已存在'''
    if request.method == 'POST':
        username = request.POST.get('params[account]')
        password = request.POST.get('params[password]')
        count = User.objects.filter(username=username).count()
        #print('POST data: ',request.POST)
        #print('path: ',request.path)
        #print('username: ',username)
        #print('password: ',password)
        #print('count of user',count)
        if count == 0:
            User.objects.create(username=username,password=password)
            return JsonResponse({'status':0})
        else:
            return JsonResponse({'status':1})
    return JsonResponse({})
