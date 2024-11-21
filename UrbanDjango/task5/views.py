from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ['user1', 'user2', 'nick']

#, class UserRegister(): pass

def process_form_data(username, password, repeat_password, age):
    error = ''
    if password != repeat_password:
        error = 'Пароли не совпадают'
    elif age < 18:
        error = 'Вы должны быть не моложе 18'
    elif username in users:
        error = 'Пользователь уже существует'
    return error

def sign_up_by_django(request):
    info = {}
    error = ''
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])
            error = process_form_data(username, password, repeat_password, age)
            if not error:
                return HttpResponse(f"<h1>Приветствуем, {username}!</h1>")
    else:
        form = UserRegister()
    info = {
        'form': form,
        'error': error,
    }
    return render(request, 'registration_page.html', context=info)

def sign_up_by_html(request):
    error = ''
    form = ''
    info = {'form': form}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        repeat_password = request.POST.get('repeat_password', '')
        age = int(request.POST.get('age', '0'))
        error = process_form_data(username, password, repeat_password, age)
        if error:
            info = {
                    'form': form,
                    'error': error,
                    'username': username,
                    'password': password,
                    'repeat_password': repeat_password,
                    'age': age
                    }
        else:
            return HttpResponse(f"<h1>Приветствуем, {username}!</h1>")

    return render(request, 'registration_page.html', context=info)
