from django.core.cache import cache

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from config.settings import CACHE_ENABLED
from .forms import CategoryForm, ProductForm, ProductModeratorForm
from .models import Product, Category
from .services import get_products_by_category


class CatalogList(ListView):
    """ Класс отображения списка продуктов. """
    model = Product
    template_name = 'catalog/catalog.html'
    context_object_name = 'products'

    def get_queryset(self):
        if not CACHE_ENABLED:
            return Product.objects.all()
        products = 'products_list'
        cached_products = cache.get(products)
        if cached_products is not None:
            return cached_products
        cached_products = Product.objects.all()
        cache.set(products, cached_products)
        return cached_products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category = Category.objects.all()
        context['categories'] = category

        return context


class ProductListByCategory(ListView):
    """ Класс отображения списка продуктов определенной категории. """
    model = Product
    template_name = 'catalog/products_by_category.html'
    context_object_name = 'products'

    def get_queryset(self):
        return get_products_by_category(self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            category = Category.objects.get(pk=self.kwargs.get('pk'))
            categories = Category.objects.all()
            context['category_name'] = category.name
            context['categories'] = categories
        except Exception:
            context['category_name'] = 'отсутствуют'
        return context


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
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.owner = self.request.user
            self.object.save()

        return super().form_valid(form)


class ProductDetail(DetailView):
    """ Класс отображения подробной информации о продукте. """
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class UpdateProduct(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """ Класс изменения данных о продукте. """

    permission_required = 'catalog.change_product'

    model = Product
    template_name = 'catalog/update_form.html'
    # form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')
    login_url = reverse_lazy('users:login')
    context_object_name = 'product'

    def get_form_class(self):
        user = self.request.user
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        if user.email == self.object.owner.email:
            return ProductForm


class DeleteProduct(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """ Класс удаления продукта. """

    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:catalog')
    login_url = reverse_lazy('users:login')
    permission_required = 'catalog.delete_product'


class Contacts(TemplateView):
    """ Класс отображения страницы Контактов. """
    template_name = "catalog/contacts.html"
