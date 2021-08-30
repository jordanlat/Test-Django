from django.urls import path

from . import views

urlpatterns = [
    path('', views.thanks, name='thanks'),
]
