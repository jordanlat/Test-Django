from django.urls import path

from . import views

urlpatterns = [
    path('', views.waiting, name='waiting'),
    path('', views.counter, name='counter'),
]
