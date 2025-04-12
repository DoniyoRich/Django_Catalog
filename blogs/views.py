from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Blog


class BlogList(ListView):
    """ Класс отображения списка статей. """
    model = Blog
    template_name = 'blogs/blogs.html'
    context_object_name = 'blogs'


class OnlyPublishedBlogs(ListView):
    """ Класс отображения только опубликованных статей. """
    model = Blog
    template_name = 'blogs/blogs.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        queryset = Blog.objects.filter(is_published=True)
        return queryset


class BlogDetail(DetailView):
    """ Класс отображения подробной информации о статье. """
    model = Blog
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class NewBlog(CreateView):
    """ Класс добавления новой статьи. """
    model = Blog
    template_name = 'blogs/blog_form.html'
    fields = ['title', 'content', 'image', 'is_published']
    success_url = reverse_lazy('blogs:blogs')


class UpdateBlog(UpdateView):
    """ Класс изменения данных о статье. """
    model = Blog
    template_name = 'blogs/Blog_form.html'
    fields = ['title', 'content', 'image', 'is_published']

    def get_success_url(self):
        return reverse('blogs:blog_detail', args=[self.kwargs.get('pk')])


class DeleteBlog(DeleteView):
    """ Класс удаления статьи. """
    model = Blog
    template_name = 'blogs/blog_confirm_delete.html'
    success_url = reverse_lazy('blogs:blogs')
