from django.contrib import admin

from blogs.models import Blog


@admin.register(Blog)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published", "created_at")
    list_filter = ("title", "is_published")
    search_fields = ("title", "content")
