from django.urls import path
from catalog import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('product_detail/', views.product_detail, name='product_detail'),

]
