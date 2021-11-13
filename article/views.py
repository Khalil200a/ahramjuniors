from django.shortcuts import render

from .models import *


def detail(request):
    articles = Article.objects.all().order_by('-id')
    context = {'articles': articles}
    return render(request, 'Articles.html', context=context)
