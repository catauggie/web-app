from django.urls import path
from . import views

#отслеживнаие различных url-адресов
urlpatterns = [
    path('', views.index, name='home'), #вызвыван из views метод index
    path('about', views.about, name='about') #переход на метод about
]
