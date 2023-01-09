from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница!!',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    #return HttpResponse("<h4>Hi</h4>") неудобно для большого кода
    return render(request, 'main/index.html', data) #шаблон  по умолчанию всегда в подпапке templates папки приложения

def about(request):
    #eturn HttpResponse("<h4>About us</h4>")
    return render(request, 'main/about.html')