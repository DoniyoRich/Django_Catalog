from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from .forms import CategoryForm, ProductForm
from .models import Product, Category


class CatalogList(ListView):
    """ Класс отображения списка продуктов. """
    model = Product
    template_name = 'catalog/catalog.html'
    context_object_name = 'products'


class NewCategory(LoginRequiredMixin, CreateView):
    """ Класс добавления новой категории. """
    model = Category
    template_name = 'catalog/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:catalog')
    login_url = reverse_lazy('users:login')


class UpdateCategory(LoginRequiredMixin, UpdateView):
    """ Класс редактирования категории. """
    model = Category
    template_name = 'catalog/category_form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('catalog:catalog')
    login_url = reverse_lazy('users:login')


class DeleteCategory(LoginRequiredMixin, DeleteView):
    """ Класс удаления категории. """
    model = Category
    template_name = 'catalog/category_confirm_delete.html'
    success_url = reverse_lazy('catalog:catalog')
    login_url = reverse_lazy('users:login')


class NewProduct(LoginRequiredMixin, CreateView):
    """ Класс добавления нового продукта. """
    model = Product
    template_name = 'catalog/product_form.html'
    # fields = ['name', 'description', 'image', 'category', 'price']
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')
    login_url = reverse_lazy('users:login')


class ProductDetail(DetailView):
    """ Класс отображения подробной информации о продукте. """
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class UpdateProduct(LoginRequiredMixin, UpdateView):
    """ Класс изменения данных о продукте. """
    model = Product
    template_name = 'catalog/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')
    login_url = reverse_lazy('users:login')


class DeleteProduct(LoginRequiredMixin, DeleteView):
    """ Класс удаления продукта. """
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:catalog')
    login_url = reverse_lazy('users:login')


class Contacts(TemplateView):
    """ Класс отображения страницы Контактов. """
    template_name = "catalog/contacts.html"
