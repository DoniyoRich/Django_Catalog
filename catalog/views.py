from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from .models import Product


class CatalogList(ListView):
    """ Класс отображения списка продуктов. """
    model = Product
    template_name = 'catalog/catalog.html'
    context_object_name = 'products'


class ProductDetail(DetailView):
    """ Класс отображения подробной информации о продукте. """
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class NewProduct(CreateView):
    """ Класс добавления нового продукта. """
    model = Product
    template_name = 'catalog/product_form.html'
    fields = ['name', 'description', 'image', 'category', 'price']
    success_url = reverse_lazy('catalog:catalog')


class UpdateProduct(UpdateView):
    """ Класс изменения данных о продукте. """
    model = Product
    template_name = 'catalog/product_form.html'
    fields = ['name', 'description', 'image', 'category', 'price']
    success_url = reverse_lazy('catalog:catalog')


class DeleteProduct(DeleteView):
    """ Класс удаления продукта. """
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:catalog')


class Contacts(TemplateView):
    """ Класс отображения страницы Контактов. """
    template_name = "catalog/contacts.html"
