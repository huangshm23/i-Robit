from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from .models import News
from django.http import JsonResponse

from model.recommendate import recommendate
from model.simulation import simulation

# Create your views here.


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


class RecommendateView(TemplateView):
    def post(self, request):
        questionnaire = request.POST.get('questionnaire')
        result = recommendate(questionnaire)
        return JsonResponse(result)


class SimulationView(TemplateView):
    def post(self, request):
        fund_ratio = request.POST.get('fund_ratio')
        result = simulation(fund_ratio)
        return JsonResponse(result)
