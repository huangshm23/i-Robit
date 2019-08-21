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
    if request.method == 'POST':
        context = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        count = User.objects.filter(username=username).count()
        if count == 0:
            context = {'status':1}
        else:
            user = User.objects.get(username=username)
            if password == user.password:
                context = {'status':0}
            else:
                context = {'status':1}
        return JsonResponse(context)
    elif request.method == 'GET':
        return JsonResponse({})


@csrf_exempt
def logout_view(request):
    '''注销视图'''
    if request.method=='GET':
        logout(request)
        context = {'status':0}
        return JsonResponse(context)

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        count = User.objects.filter(username=username).count()
        if count == 0:
            User.objects.create(username=username,password=password)
            return JsonResponse({'status':0,'msg':''})
        else:
            return JsonResponse({'status':1,'msg':'用户名已存在'})
    elif request.method=='GET':
        return JsonResponse({})
