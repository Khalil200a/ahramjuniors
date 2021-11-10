from django.shortcuts import render

from .models import *

def detail(request):
    news =News.objects.order_by('-id')[:3]
    context = {'news': news}
    return render(request, 'index.html', context=context)
