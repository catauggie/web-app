from django.shortcuts import render
from .models import Articles

def news_home(request):
    #news = Articles.objects.all() #получаем все объекты в табличке Articles
    news = Articles.objects.order_by('-title')  # сортируем статьи по названию; data- по дате
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    return render(request, 'news/create.html')