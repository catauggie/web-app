from django.urls import path
from . import views

#отслеживнаие различных url-адресов
urlpatterns = [
    path('', views.news_home, name='news_home'), #отслеживаем пустую строку, поскольку после перехода на news оказываемся и так внутри папки
    # если в '' что вписать, например еще раз news, то будет http://127.0.0.1:8000/news/news; при этом на http://127.0.0.1:8000/news будет ошибка
    path('create', views.create, name='create')  #http://127.0.0.1:8000/news/create
]
