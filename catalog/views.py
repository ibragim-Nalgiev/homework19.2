from django.shortcuts import render

from catalog.models import Product


def home(request):
    context = {
        'object_list': Product.objects.all()
    }

    return render(request, 'catalog/home.html', context)

def product_detail(request):
    context = {
        'object_list': Product.objects.all()
    }

    return render(request, 'catalog/product_detail.html', context)




def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name} ({phone}, {message})")
    return render(request, 'catalog/contacts.html')
