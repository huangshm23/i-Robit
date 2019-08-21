from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from .models import News
from django.http import JsonResponse

from model.recommendate import recommendate
from model.simulation import simulation
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class NewsView(TemplateView):

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
class RecommendateView(TemplateView):
    def post(self, request):
        body=json.loads(request.body)
        questionnaire = body.get('questionnaire')
        result = recommendate(questionnaire)
        return JsonResponse(result)


@method_decorator(csrf_exempt, name='dispatch')
class SimulationView(TemplateView):
    def post(self, request):
        body=json.loads(request.body)
        fund_ratio = body.get('fund_ratio')
        result = simulation(fund_ratio)
        return JsonResponse(result)
