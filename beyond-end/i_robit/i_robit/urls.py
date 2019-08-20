"""i_robit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from i_robot.views import NewsView, RecommendateView, SimulationView

urlpatterns = [
    path('admin/', admin.site.urls),
    # 用户系统的URL
    path('users/', include('users.urls', namespace='users')),
    # 连接前端代码
    path('', TemplateView.as_view(template_name="index.html")),
    re_path('news/(?P<news_id>[0-9]+)?$', NewsView.as_view()),
    path('recommendate', RecommendateView.as_view()),
    path('simulation', SimulationView.as_view())
]
