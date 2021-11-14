from django.shortcuts import render

from .models import *


def detail(request):
    articles = Article.objects.all().order_by('-id')
    recent = Article.objects.order_by('-id')[:4]
    context = {'articles': articles, 'recent': recent}
    return render(request, 'Articles.html', context=context)
