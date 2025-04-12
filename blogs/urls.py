from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import NewBlog, BlogDetail, UpdateBlog, DeleteBlog, BlogList, OnlyPublishedBlogs

app_name = BlogsConfig.name

urlpatterns = [
    path("", BlogList.as_view(), name="blogs"),
    path("only_published/", OnlyPublishedBlogs.as_view(), name="only_published"),
    path("new_blog/", NewBlog.as_view(), name="new_blog"),
    path("blog_detail/<int:pk>", BlogDetail.as_view(), name="blog_detail"),
    path("update_blog/<int:pk>", UpdateBlog.as_view(), name="update_blog"),
    path("delete_blog/<int:pk>", DeleteBlog.as_view(), name="delete_blog"),
]
