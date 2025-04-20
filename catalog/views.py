from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from .forms import CategoryForm, ProductForm
from .models import Product, Category


class CatalogList(ListView):
    """ Класс отображения списка продуктов. """
    model = Product
    template_name = 'catalog/catalog.html'
    context_object_name = 'products'


class NewCategory(CreateView):
    """ Класс добавления новой категории. """
    model = Category
    template_name = 'catalog/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:catalog')


class UpdateCategory(UpdateView):
    """ Класс редактирования категории. """
    model = Category
    template_name = 'catalog/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:catalog')


class DeleteCategory(DeleteView):
    """ Класс удаления категории. """
    model = Category
    template_name = 'catalog/category_confirm_delete.html'
    success_url = reverse_lazy('catalog:catalog')


class NewProduct(CreateView):
    """ Класс добавления нового продукта. """
    model = Product
    template_name = 'catalog/product_form.html'
    # fields = ['name', 'description', 'image', 'category', 'price']
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')
    

class ProductDetail(DetailView):
    """ Класс отображения подробной информации о продукте. """
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class UpdateProduct(UpdateView):
    """ Класс изменения данных о продукте. """
    model = Product
    template_name = 'catalog/product_form.html'
    # fields = ['name', 'description', 'image', 'category', 'price']
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')


class DeleteProduct(DeleteView):
    """ Класс удаления продукта. """
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:catalog')


class Contacts(TemplateView):
    """ Класс отображения страницы Контактов. """
    template_name = "catalog/contacts.html"
