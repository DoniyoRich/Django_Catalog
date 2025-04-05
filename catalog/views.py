from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Product


def catalog(request) -> HttpResponse:
    """
    Функция возвращает страницу catalog.html.
    """
    products = Product.objects.all()
    context = {'products': products}

    return render(request, "catalog/catalog.html", context=context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}

    return render(request, "catalog/product_detail.html", context=context)


def contacts(request) -> HttpResponse:
    """
    Функция возвращает страницу contacts.html.
    """
    return render(request, "catalog/contacts.html")
