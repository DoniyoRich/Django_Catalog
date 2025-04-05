from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.catalog, name="catalog"),
    path("product_detail/<int:pk>", views.product_detail, name="product_detail"),
    path("contacts/", views.contacts, name="contacts"),
]
