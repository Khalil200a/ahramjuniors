from django.urls import path

from . import views

urlpatterns = [
    path('join/', views.detailjoin, name='join'),
    path('donate/', views.detaildonate, name='donate'),
]