from django.shortcuts import render

from .models import *
from article.models import *


def detail(request):
    events = Event.objects.all().order_by('-id')
    recent = Article.objects.order_by('-id')[:4]
    context = {'Events': events, 'recent': recent}
    return render(request, 'Work.html', context=context)
