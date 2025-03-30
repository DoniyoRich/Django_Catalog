from django.http import HttpResponse
from django.shortcuts import render


def home(request) -> HttpResponse:
    """
    Функция возвращает страницу home.html.
    """
    return render(request, "catalog/home.html")


def contacts(request) -> HttpResponse:
    """
    Функция возвращает страницу contacts.html.
    """
    return render(request, "catalog/contacts.html")
