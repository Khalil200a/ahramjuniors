from django.shortcuts import render

from article.models import *


def detailjoin(request):
    recent = Article.objects.order_by('-id')[:4]
    context = {'recent': recent}
    return render(request, 'join.html', context=context)


def detaildonate(request):
    recent = Article.objects.order_by('-id')[:4]
    context = {'recent': recent}
    return render(request, 'donate.html', context=context)
