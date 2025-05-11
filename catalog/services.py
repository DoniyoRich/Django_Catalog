from catalog.models import Product
from django.shortcuts import redirect


def get_products_by_category(pk):
    products_by_category = Product.objects.filter(category_id=pk)
    return products_by_category


def handle_category_selection(request):
    if request.method == 'POST':
        category_id = request.POST.get('category')
        return redirect('catalog:product_by_category', pk=category_id)
