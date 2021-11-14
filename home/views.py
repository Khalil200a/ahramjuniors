from django.shortcuts import render

from .models import *
from event.models import *
from article.models import *

def detail(request):
    news =News.objects.order_by('-id')[:3]
    events = Event.objects.all().order_by('-id')
    recent = Article.objects.order_by('-id')[:4]
    context = {'news': news, 'Events': events, 'recent': recent}
    return render(request, 'index.html', context=context)
