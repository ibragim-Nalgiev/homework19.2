from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogDeleteView, BlogUpdateView, BlogDetailView, BlogCreateView, BlogListView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<slug:the_slug>/', BlogDetailView.as_view(), name='blog_item'),
    path('blog/update/<slug:the_slug>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<slug:the_slug>/', BlogDeleteView.as_view(), name='blog_delete'),

]
