from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from .models import Product


class CatalogList(ListView):
    model = Product
    template_name = 'catalog/catalog.html'
    context_object_name = 'products'


class ProductDetail(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class NewProduct(CreateView):
    model = Product
    template_name = 'catalog/product_form.html'
    fields = ['name', 'description', 'image', 'category', 'price']
    success_url = reverse_lazy('catalog:catalog')


class UpdateProduct(UpdateView):
    model = Product
    template_name = 'catalog/product_form.html'
    fields = ['name', 'description', 'image', 'category', 'price']
    success_url = reverse_lazy('catalog:catalog')


class DeleteProduct(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:catalog')


class Contacts(TemplateView):
    template_name = "catalog/contacts.html"

# def contacts(request) -> HttpResponse:
#     """
#     Функция возвращает страницу contacts.html.
#     """
#     return render(request, "catalog/contacts.html")

# def catalog(request) -> HttpResponse:
#     """
#     Функция возвращает страницу catalog.html.
#     """
#     products = Product.objects.all()
#     context = {'products': products}
#
#     return render(request, "catalog/catalog.html", context=context)
#
#
# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#
#     return render(request, "catalog/product_detail.html", context=context)
#
#
