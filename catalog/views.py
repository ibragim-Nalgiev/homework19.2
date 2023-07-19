from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/catalog_list.html'


def product_detail(request):
    context = {
        'object_list': Product.objects.all()
    }

    return render(request, 'catalog/catalog_product_detail.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name} ({phone}, {message})")
    return render(request, 'catalog/contacts.html')
