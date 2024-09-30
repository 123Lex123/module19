from django.shortcuts import render, redirect
from .forms import UserRegister
from .models import Buyer
from .models import Game


def shop_page(request):
    games = Game.objects.all()
    return render(request, 'task1/shop_page.html', {'games': games})


def main_page(request):
    return render(request, 'task1/main_page.html')


def cart_page(request):
    return render(request, 'task1/cart_page.html')


def sign_up_by_html(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            age = form.cleaned_data['age']

            # Проверка, существует ли пользователь с таким именем
            existing_buyers = Buyer.objects.filter(name=username)

            if not existing_buyers:
                # Если пользователь не существует, создаем его
                Buyer.objects.create(name=username, balance=0, age=age)
                return redirect('main_page')  # После успешной регистрации
            else:
                form.add_error('username', 'Пользователь с таким именем уже существует.')
    else:
        form = UserRegister()

    return render(request, 'task1/registration_page.html', {'form': form})
