
from django.urls import reverse_lazy, reverse
from django.views import generic

from blog.models import Blog


class BlogListView(generic.ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    slug_url_kwarg = 'the_slug'
    slug_field = 'slug'
    success_url = reverse_lazy('blog:blog_list')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'image', 'is_published')
    success_url = reverse_lazy('blog:blog_list')
    template_name = 'blog/blog_form.html'


class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'image', 'is_published')
    template_name = 'blog/blog_form.html'
    slug_url_kwarg = 'the_slug'
    slug_field = 'slug'

    def get_success_url(self):
        return reverse('blog:blog_item', kwargs={'the_slug': self.object.slug})


class BlogDeleteView(generic.DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')
    template_name = 'blog/blog_confirm_delete.html'
    slug_url_kwarg = 'the_slug'
    slug_field = 'slug'
