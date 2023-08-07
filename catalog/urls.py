from django.urls import path
from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import ProductCreateView, ProductUpdateView, ProductDeleteView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),


]
