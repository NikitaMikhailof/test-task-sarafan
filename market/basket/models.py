from django.contrib.auth.models import User
from django.db import models
from product.models import Product


# Create your models here.
class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class UserBasket(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, verbose_name='Корзина')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')

    def __str__(self):
        return f'{self.product.title} ({self.quantity} шт.)'

    class Meta:
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = 'Продукты в корзинах'