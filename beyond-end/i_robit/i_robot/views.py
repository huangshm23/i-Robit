#from django.shortcuts import render
from django.db.models import Q
from .models import News
from django.http import JsonResponse

from model.interface import recommendate,simulation

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from auth import Authtication

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class NewsView(APIView):
    authentication_classes = [Authtication,]
    def get(self, request, news_id):

        if news_id:
            news_id = int(news_id)
            try:
                news = News.objects.get(id=news_id)
            except News.DoesNotExist:
                return JsonResponse({'status': 0})
        else:
            news = News.objects.order_by("?").first()
            news_id = news.id

        other_news = News.objects.filter(~Q(id=news_id)).order_by("?")[:2]
        json_list = {
            'status': 1,
            'title': news.title,
            'datetime': news.time,
            'source_url': news.url,
            'source': news.source,
            'news_body': news.newspaper,
            'next_title': other_news[0].title,
            'pre_title': other_news[1].title,
            'next_url': other_news[0].id,
            'pre_url': other_news[1].id
        }
        return JsonResponse(json_list)


@method_decorator(csrf_exempt, name='dispatch')
class RecommendateView(APIView):

    authentication_classes = [Authtication,]

    def post(self, request):
        questionnaire = request.data['questionnaire']
        questionnaire=list(questionnaire.split(','))
        result = recommendate(questionnaire)
        if result != {}:
            recommendation = eval(result['recommendation'])
            result['recommendation'] = []
            for name,ratio in recommendation.items():
                fund = {'name':name,'ratio':ratio}
                result['recommendation'].append(fund)
        return JsonResponse(result)
        
    def get(self, request):
        return JsonResponse({})


@method_decorator(csrf_exempt, name='dispatch')
class SimulationView(APIView):

    authentication_classes = [Authtication,]

    def post(self, request):
        fund_ratio = eval(request.data['fund_ratio'])   
        result = simulation(fund_ratio)
        if result is None:
            return JsonResponse({'status':1,'err':'权值和不为1'})
        return JsonResponse(result)

    def get(self, request):
        return JsonResponse({})
