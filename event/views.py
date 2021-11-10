from django.shortcuts import render

from .models import *

def detail(request):
    context = {}
    return render(request, 'Work.html', context=context)
