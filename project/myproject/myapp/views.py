from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Hello, world')

def about(request):
    return HttpResponse('about us')

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    html = """
    <h1>Добро пожаловать на мой Django-сайт!</h1>
    <p>Это главная страница моего сайта.</p>
    """
    return HttpResponse(html)

def about(request):
    html = """
    <h1>Обо мне</h1>
    <p>Привет! Меня зовут Олег. Я учусь создавать веб-приложения с помощью Django.
        Я работаю главным специалистом отдела геодезии на строительстве атомной станции "Аккую" в Турецкой республике.</p>
    """
    return HttpResponse(html)