from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.services import handle_category_selection
from catalog.views import CatalogList, ProductDetail, Contacts, NewProduct, UpdateProduct, DeleteProduct, NewCategory, \
    UpdateCategory, DeleteCategory, ProductListByCategory

app_name = CatalogConfig.name

urlpatterns = [
    path("", CatalogList.as_view(), name="catalog"),
    path('handle-selection/', handle_category_selection, name='handle_category_selection'),
    path("products_by_category/<int:pk>", ProductListByCategory.as_view(), name="product_by_category"),

    path("new_category/", NewCategory.as_view(), name="new_category"),
    path("update_category/<int:pk>", UpdateCategory.as_view(), name="update_category"),
    path("delete_category/<int:pk>", DeleteCategory.as_view(), name="delete_category"),

    path("new_product/", NewProduct.as_view(), name="new_product"),
    path("product_detail/<int:pk>", cache_page(60)(ProductDetail.as_view()), name="product_detail"),
    path("update_product/<int:pk>", UpdateProduct.as_view(), name="update_product"),
    path("delete_product/<int:pk>", DeleteProduct.as_view(), name="delete_product"),
    path("contacts/", Contacts.as_view(), name="contacts"),
]
