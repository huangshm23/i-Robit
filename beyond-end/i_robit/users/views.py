from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password, check_password
from .models import User,Email_auth
import random

# Create your views here.

from django.views.decorators.csrf import csrf_exempt

#获取随机激活码
def get_activate_id(id_length=6):
    seq = '0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    length = len(seq)-1
    activate_id = ''
    for i in range(id_length):
        ind = random.randint(0,length)
        activate_id += seq[ind]
    return activate_id

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
            if user.is_active == False:
                context = {'status':2}    #账号未激活
            else:
                if check_password(password,user.password):
                    context = {'status':0}
                else:
                    context = {'status':1}  #账户或密码错误
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
        
        #先生成可能要发送的邮件信息
        email_to = username
        activate_id = get_activate_id()
        title = 'i-Robot注册验证'
        message = '欢迎注册i-Robot，请点击此链接激活账号：http://178.128.115.175:80/activate/{0}'.format(activate_id)
        email_from = 'huaqi_irobot@163.com'
        reciever = [email_to]
        
        count = User.objects.filter(username=username).count()
        if count!=0:
            user = User.objects.get(username=username)
            if user.is_active == True:  #已经注册且激活
                return JsonResponse({'status':1,'msg':'用户名已存在'})

        #未注册 或者 未激活 都要发送激活邮件
        try:
            send_mail(title,message,email_from,reciever)
            Email_auth.objects.create(activate_id=activate_id,email=email_to)
        except:
            return JsonResponse({'status':2,'msg':'邮箱不存在'})
        #如果是未注册，这是已经验证邮箱合法，可以将用户信息存进数据库
        if count == 0:
            User.objects.create(username=username,password=make_password(password,None,'pbkdf2_sha1'),is_active=False)
        return JsonResponse({'status':0,'msg':''})
    
    elif request.method=='GET':
        return JsonResponse({})

#账户激活视图
def activate_view(request,activate_id):
    if request.method == 'GET':
        try:
            Email_user = Email_auth.objects.get(activate_id=activate_id)
            username = Email_user.email
            user = User.objects.get(username=username)
            user.is_active = True
            user.save()
            Email_user.delete()
            return JsonResponse({'status':0})
        except Email_auth.DoesNotExist:
            return JsonResponse({'status':1})
