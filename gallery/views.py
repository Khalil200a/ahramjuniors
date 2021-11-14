from django.shortcuts import render

from .models import *
from article.models import *


def detail(request):
    photo = Photo.objects.all().order_by('-id')
    video = Video.objects.all().order_by('-id')
    recent = Article.objects.order_by('-id')[:4]
    context = {'photos': photo, 'videos': video, 'recent': recent}
    return render(request, 'gallery.html', context=context)
