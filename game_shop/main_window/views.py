from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db.utils import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from .routing_logic import create_new_user, check_user, create_order, get_user_orders
import bs4 as BeautifulSoup


def show_regpage(request):
    return render(request, 'regpage.html')

def show_homepage(request):
    return render(request, 'homepage.html')

def show_orderpage_archam(request):
    return render(request, 'orders_archam.html')

def show_orderpage_caribian(request):
    return render(request, 'orders_caribian.html')

def show_orderpage_cringe(request):
    return render(request, 'orders_cringe.html')

def show_my_orders(request):
    return render(request, 'my_orders.html')

def checkuser(request):
    try:
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            resp = check_user(email=email, password=password)
            data = {
                'email': email,
                'password': password,
            }
            match resp:
                case 1:
                    return HttpResponseRedirect('http://127.0.0.1:8000/')
                case 0:
                    messages.error(request, 'ничего не найдено')
                    # return render(request, "authpage.html", data)
    except IntegrityError:
        data = {
            'email': email,
            'password': password,
        }
        messages.error(request, 'ничего не найдено')
        return render(request, "authpage.html", data)

def sign_up(request):
    try:
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            resp = create_new_user(email=email, password=password)
            data = {
                'email': email,
                'password': password,
            }
            match resp:
                case 'success':
                    messages.error(request, 'Вы успешно зарегистрированы')
                    return render(request, "regpage.html", data)
                case 'unsuccess':
                    messages.error(request, 'Ошибка, проверьте введенные данные')
                    return render(request, "regpage.html", data)
    except IntegrityError:
        data = {
            'email': email,
            'password': password,
        }
        messages.error(request, 'Ошибка, проверьте введенные данные')
        return render(request, "regpage.html", data)

def create_order_caribian(request):
    try:
        if request.method == "POST":
            game_name = request.POST.get("game_name")
            price = request.POST.get("price")
            email = request.POST.get("email")
            order_state = create_order(email=email, game_name=game_name, price=price)
            data = {
                'game_name': game_name,
                'price': price,
                'email': email,
            }
            match order_state:
                case 'success':
                    messages.error(request, 'Заказ создан')
                    return render(request, "orders_caribian.html", data)
                case 'unsuccess':
                    messages.error(request, 'Заказ не создан')
                    return render(request, "orders_caribian.html", data)
    except IntegrityError:
        data = {
            'game_name': game_name,
            'price': price,
            'email': email,
        }
        messages.error(request, 'Ошибка, проверьте введенные данные')
        return render(request, "orders_caribian.html", data)

def create_order_archam(request):
    try:
        if request.method == "POST":
            game_name = request.POST.get("game_name")
            price = request.POST.get("price")
            email = request.POST.get("email")
            order_state = create_order(email=email, game_name=game_name, price=price)
            data = {
                'game_name': game_name,
                'price': price,
                'email': email,
            }
            match order_state:
                case 'success':
                    messages.error(request, 'Заказ создан')
                    return render(request, "orders_archam.html", data)
                case 'unsuccess':
                    messages.error(request, 'Заказ не создан')
                    return render(request, "orders_archam.html", data)
    except IntegrityError:
        data = {
            'game_name': game_name,
            'price': price,
            'email': email,
        }
        messages.error(request, 'Ошибка, проверьте введенные данные')
        return render(request, "orders_archam.html", data)

def create_order_cringe(request):
    try:
        if request.method == "POST":
            game_name = request.POST.get("game_name")
            price = request.POST.get("price")
            email = request.POST.get("email")
            order_state = create_order(email=email, game_name=game_name, price=price)
            data = {
                'game_name': game_name,
                'price': price,
                'email': email,
            }
            match order_state:
                case 'success':
                    messages.error(request, 'Заказ создан')
                    return render(request, "orders_cringe.html", data)
                case 'unsuccess':
                    messages.error(request, 'Заказ не создан')
                    return render(request, "orders_cringe.html", data)
    except IntegrityError:
        data = {
            'game_name': game_name,
            'price': price,
            'email': email,
        }
        messages.error(request, 'Ошибка, проверьте введенные данные')
        return render(request, "orders_cringe.html", data)

def get_my_orders(request):
    try:
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            user_status = check_user(email=email, password=password)
            data = {
                'email': email,
                'password': password
            }
            match user_status:
                case 1:
                    user_orders = get_user_orders(email=email)
                    if user_orders:
                        for item in user_orders:
                            messages.error(request,
                                           f"номер заказа: {item[0]} название игры: {item[1]} цена: {item[2]}, дата: {item[3]}\n")
                        data['orders'] = user_orders
                        return render(request, "my_orders.html", data)
                    else:
                        messages.error(request, 'Заказов не найдено')
                        return render(request, "my_orders.html", data)
                case 0:
                    messages.error(request, 'Ошибка, проверьте введенныe данные')
                    return render(request, "my_orders.html", data)
    except IntegrityError:
        data = {
            'email': email,
            'password': password
        }
        messages.error(request, 'Ошибка, проверьте введенные данные')
        return render(request, "my_orders.html", data)