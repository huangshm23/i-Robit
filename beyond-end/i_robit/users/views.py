from django.http import JsonResponse
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password, check_password
from .models import User,Email_auth,UserToken
# 装饰器
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

#rest_framework
from rest_framework.views import APIView

#自定义
from auth import Generete_token,Authtication,get_activate_id,VisitThrottle


@method_decorator(csrf_exempt, name='dispatch')
class Login(APIView):
    '''登录视图'''
    def post(self,request):
        context = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        count = User.objects.filter(username=username).count()
        if count == 0:
            context = {'status':1}
            print('账号不存在')
        else:
            user = User.objects.get(username=username)
            if user.is_active == False:
                context = {'status':2}    #账号未激活
                print('账号未激活')
            else:
                if check_password(password,user.password):
                    context = {'status':0}
                    print('密码正确')
                    token = Generete_token(username)
                    print('生成token: ',token)
                    context['token']=token
                    user.token = token
                    user.save()
                    UserToken.objects.update_or_create(user=user,defaults={'token':token})
                else:
                    context = {'status':1}  #账户或密码错误
                    print('密码错误')
        return JsonResponse(context)
    
    def get(self,request):
        return JsonResponse({})


@method_decorator(csrf_exempt, name='dispatch')
class Logout(APIView):
    '''注销视图'''
    authentication_classes = [Authtication,]
    def get(self,request):
        #print(request.user)
        #print(request.auth)
        #logout(request) #注销函数
        #删除用户对应的Token
        token = request._request.GET.get('token')
        token_obj = UserToken.objects.get(token=token)
        token_obj.delete()
        return JsonResponse({'status':0})


@method_decorator(csrf_exempt, name='dispatch')
class Register(APIView):
    '''注册视图'''
    throttle_classes = [VisitThrottle,] #一分钟内只能注册三次
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        count = User.objects.filter(username=username).count()

        #先生成可能要发送的邮件信息
        email_to = username
        activate_id = get_activate_id()
        title = 'i-Robot注册验证'
        #message = '欢迎注册irobot，请点击此链接激活账号：http://178.128.115.175:80/activate/{0}'.format(activate_id)
        message = '欢迎注册irobot，请点击此链接激活账号：http://127.0.0.1:8000/activate/{0}'.format(activate_id)
        #email_from = 'irobot2019@sina.com'
        email_from = '986439206@qq.com'
        reciever = [email_to]    
        
        count = User.objects.filter(username=username).count()
        if count!=0:
            user = User.objects.get(username=username)
            if user.is_active == True:  #已经注册且激活
                print('账号已经注册好了')
                return JsonResponse({'status':1,'msg':'用户名已存在'})

        #未注册 或者 未激活 都要发送激活邮件
        try:
            sendstatus = send_mail(title,message,email_from,reciever)
            print('邮件发送状态:',sendstatus)
            Email_auth.objects.create(activate_id=activate_id,email=email_to)
        except:
            return JsonResponse({'status':2,'msg':'邮箱不存在'})
        #如果是未注册，这是已经验证邮箱合法，可以将用户信息存进数据库
        if count == 0:
            print('创建账号但未激活')
            User.objects.create(username=username,password=make_password(password,None,'pbkdf2_sha1'),is_active=False)
        else:
            print('账号已经创建但未激活')
        return JsonResponse({'status':0,'msg':''})

    def get(self,request):
        return JsonResponse({})


@method_decorator(csrf_exempt, name='dispatch')
class Activate(APIView):
    '''账户激活视图'''
    def get(self,request,activate_id):
        print('activate_id: ',activate_id)
        Email_user = Email_auth.objects.filter(activate_id=activate_id).first()
        if Email_user is not None:
            username = Email_user.email
            user = User.objects.get(username=username)
            user.is_active = True
            user.save()
            Email_user.delete()
            return JsonResponse({'status':0})   #激活成功
        return JsonResponse({'status':1})           #激活失败
