from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CatalogList, ProductDetail, Contacts, NewProduct, UpdateProduct, DeleteProduct

app_name = CatalogConfig.name

urlpatterns = [
    path("", CatalogList.as_view(), name="catalog"),
    path("new_product/", NewProduct.as_view(), name="new_product"),
    path("product_detail/<int:pk>", ProductDetail.as_view(), name="product_detail"),
    path("update_product/<int:pk>", UpdateProduct.as_view(), name="update_product"),
    path("delete_product/<int:pk>", DeleteProduct.as_view(), name="delete_product"),
    path("contacts/", Contacts.as_view(), name="contacts"),
]
