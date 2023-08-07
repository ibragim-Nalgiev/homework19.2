from django.core.exceptions import ValidationError
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('pk',)


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='media/', verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_change_date = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f"Наименование товара: {self.title}. " \
               f"Категория: {self.category}. " \
               f"Цена: {self.price}. " \
               f"Дата создания: {self.create_date}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('pk',)


class Version(models.Model):

    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='version', verbose_name='Продукт')
    version_number = models.IntegerField(verbose_name='Версия')
    version_title = models.CharField(max_length=250, verbose_name='Название версии')
    is_active = models.BooleanField(default=True, verbose_name='Признак активности')

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ('pk',)

    def __str__(self):
        return f"{self.version_title} {self.product}"


