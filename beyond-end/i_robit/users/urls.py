'''用户系统URL模式'''

from django.urls import path 
from . import views
#from django.contrib.auth.views import LoginView

# LoginView.template_name = 'users/login.html'
app_name = 'users'

urlpatterns = [
    #登录(可以用Django自带的视图:LoginView.as_view(),然后指定模板的路径)
    path('login/',views.login_view,name='login'),
    #注销
    path('logout/',views.logout_view,name='login'),
    #注册
    path('register/',views.register_view,name='register')
]
