from click import password_option
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from events.models import User
from django.core.exceptions import ObjectDoesNotExist

events = [
    {'id': 1, 'name': 'Преступление и наказание', 'place': 'Большой театр', 'date': '21-07-2025'},
    {'id': 2, 'name': 'Как закалялась сталь', 'place': 'Мариинский театр', 'date': '13-08-2025'}
]

def index(request):
    data = {
        'title': 'Главная страница',
        'events': events,
        'user': request.session.get('user'),
    }

    if (request.POST.get('action') == 'Regist'):
        login = request.POST.get('login')
        pswd = request.POST.get('password')
        user = User(login=login, password=pswd)
        user.save()

        data['user'] = user.login
        request.session['user'] = user.login

    elif (request.POST.get('action') == 'Login'):

        try:
            user = User.objects.get(login=request.POST.get('login'), password=request.POST.get('password'))

            data['user'] = user.login
            request.session['user'] = user.login

        except ObjectDoesNotExist:

            return redirect('login')

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