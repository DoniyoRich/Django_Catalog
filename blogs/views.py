from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Blog


class BlogList(ListView):
    """ Класс отображения списка продуктов. """
    model = Blog
    template_name = 'blogs/blogs.html'
    context_object_name = 'blogs'


class BlogDetail(DetailView):
    """ Класс отображения подробной информации о продукте. """
    model = Blog
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'blog'


class NewBlog(CreateView):
    """ Класс добавления нового продукта. """
    model = Blog
    template_name = 'blogs/blog_form.html'
    fields = ['title', 'content', 'image', 'is_published']
    success_url = reverse_lazy('blogs:blogs')


class UpdateBlog(UpdateView):
    """ Класс изменения данных о продукте. """
    model = Blog
    template_name = 'blogs/Blog_form.html'
    fields = ['title', 'content', 'image', 'is_published']
    success_url = reverse_lazy('blogs:blogs')


class DeleteBlog(DeleteView):
    """ Класс удаления продукта. """
    model = Blog
    template_name = 'blogs/blog_confirm_delete.html'
    success_url = reverse_lazy('blogs:blogs')

# class Contacts(TemplateView):
#     """ Класс отображения страницы Контактов. """
#     template_name = "catalog/contacts.html"
