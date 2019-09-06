import hashlib
import random
from datetime import datetime,timedelta
from django.core.cache import cache
from django.utils.timezone import utc
from django.http import JsonResponse
from users.models import UserToken
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.throttling import SimpleRateThrottle
from rest_framework.views import exception_handler as django_exception_handler


#让所有异常返回json格式以便前端接收
def exception_handler(exception,context):
    '''自定义异常处理'''
    response = django_exception_handler(exception,context)
    if response is None:
        return JsonResponse({'status':0,'err':'服务器内部错误'})
    return JsonResponse({'status':2019,'err':'异常处理'})


#获取随机激活码
def get_activate_id(id_length=8):
    seq = '0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    length = len(seq)-1
    activate_id = ''
    for i in range(id_length):
        ind = random.randint(0,length)
        activate_id += seq[ind]
    return activate_id

def Generete_token(user):
    #user: 用户名,字符串类型
    #用户名的唯一性保证了token的唯一性
    random_str = get_activate_id()
    token = hashlib.md5(bytes(user,encoding='utf-8'))
    token.update(bytes(user,encoding='utf-8'))
    token.update(bytes(random_str,encoding='utf-8'))
    return token.hexdigest()

class Authtication(BaseAuthentication):
    
    def authenticate(self,request):
        token = request._request.GET.get('token')

        token_obj = cache.get(token,None)
        if token_obj:
            return (token_obj.user,token_obj)

        token_obj = UserToken.objects.filter(token=token).first()
        if token_obj is None:
            raise exceptions.AuthenticationFailed('用户认证失败')
        
        cur_time = datetime.utcnow().replace(tzinfo=utc)

        if cur_time - timedelta(hours=6)>token_obj.created_time:
            token_obj.delete()
            raise exceptions.AuthenticationFailed('token失效')

        cache.set(token,token_obj,100)   

        return (token_obj.user,token_obj)

    
    def authenticate_header(self,request):
        pass

#继承了SimpleRateThrottle则直接使用了django内置的缓存
class VisitThrottle(SimpleRateThrottle):
    scope = 'irobot'

    def get_cache_key(self,request,view):
        return self.get_ident(request) #IP作为唯一标识

