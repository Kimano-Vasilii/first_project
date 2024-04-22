from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os
def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': '',
        'Показать содержимое рабочей директории': ''
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    msg = f'Текущее время: {formatted_time}'
    return HttpResponse(msg)


def workdir_view(request):
    current_dir = os.getcwd()
    files = os.listdir(current_dir)
    files_str = '\n'.join(files)
    return HttpResponse(files_str)
