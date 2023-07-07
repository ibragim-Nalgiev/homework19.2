from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **kwargs):


        Laptops = Category.objects.get(title='Ноутбуки')
        Phones = Category.objects.get(title='Телефоны')
        Watch = Category.objects.get(title='Часы')

        products_list = [
            {'title': 'Макбук Про', 'description': 'Модель 2019 года',
             'image': 'media/images/macbookpro.jpg', 'category': Laptops, 'price': 70000.0},
            {'title': 'Айфон', 'description': 'Последний айфон 14 на 256 гб',
             'image': 'media/images/iphone14.webp', 'category': Phones, 'price': 102000.0},
            {'title': 'Эпл Ватч', 'description': 'Мужские часы',
             'image': 'media/images/Apple-Watch.jpg', 'category': Watch, 'price': 30000.0}
        ]

        Product.objects.all().delete()

        products_for_create = []

        for product in products_list:
            products_for_create.append(
                Product(**product)
            )

        Product.objects.bulk_create(products_for_create)