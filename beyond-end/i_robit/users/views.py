from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
import json

from .forms import LoginForm
# Create your views here.

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def login_view(request):
    '''登录视图'''
    if request.method == 'POST':
        body=json.loads(request.body)
        login_form = LoginForm(body)
        if login_form.is_valid():
            username = body.get('account')
            passsword = body.get('password')
            user = authenticate(username=username, passsword=passsword)
            if user:
                login(request, user)
                return JsonResponse({'status': 0})
            else:
                match = 2
        else:
            match = 1
        context = {'status':match}
        return JsonResponse(context) 
    else:   #不是POST请求就返回一个空表单
        context = {'status':1}
        return JsonResponse(context)

def logout_view(request):
    '''注销视图'''
    logout(request)
    context = {'status':0}
    return JsonResponse(context)

def register_view(request):
    if request.method == 'GET':
        return {}
    else:
        body=json.loads(request.body)
        form = UserCreationForm(data=body)
        if form.is_valid():
            new_user = form.save()
            return JsonResponse({'status': 1,'msg':''})
        else:
            errors=dict(form.errors.items())
            return JsonResponse({'status': 0,'msg':list(errors.values())[0]})
