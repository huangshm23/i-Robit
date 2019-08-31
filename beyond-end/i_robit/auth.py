import hashlib
import random
from users.models import UserToken
from rest_framework import exceptions

#获取随机激活码
def get_activate_id(id_length=6):
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

class Authtication():
    
    def authenticate(self,request):
        token = request._request.GET.get('token')
        token_obj = UserToken.objects.filter(token=token).first()
        if token_obj is None:
            raise exceptions.AuthenticationFailed('用户认证失败')
        #双重验证: token是否存在 以及 token和用户是否对应
        user = token_obj.user
        if user.token != token:
            raise exceptions.AuthenticationFailed('用户认证失败')

        return (user,token_obj)
    
    def authenticate_header(self,request):
        pass
