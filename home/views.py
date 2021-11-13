from django.shortcuts import render

from .models import *
from event.models import *

def detail(request):
    news =News.objects.order_by('-id')[:3]
    events = Event.objects.all().order_by('-id')
    context = {'news': news, 'Events': events}
    return render(request, 'index.html', context=context)
