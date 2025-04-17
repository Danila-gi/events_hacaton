from click import password_option
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from events.models import User

events = [
    {'id': 1, 'name': 'Преступление и наказание', 'place': 'Большой театр', 'date': '21-07-2025'},
    {'id': 2, 'name': 'Как закалялась сталь', 'place': 'Мариинский театр', 'date': '13-08-2025'}
]

def index(request):
    if (request.POST):
        login = request.POST['login']
        pswd = request.POST['password']
        user = User(login=login, password=pswd)
        user.save()

    data = {
        'title': 'Главная страница',
        'events': events
    }
    return render(request, 'events/index.html', data)

def registration(request):
    data = {'title': 'Регистрация'}
    return render(request, 'events/regist.html', data)

def login(request):
    data = {'title': 'Вход'}
    return render(request, 'events/login.html', data)

def event(request, event_id):
    return HttpResponse(f"Event with id = {event_id}")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Not found this URL!!!</h1>")