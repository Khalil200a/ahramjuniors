from django.shortcuts import render

from .models import *


def detail(request):
    events =Event.objects.all().order_by('-id')
    context = {'Events': events}
    return render(request, 'Work.html', context=context)
