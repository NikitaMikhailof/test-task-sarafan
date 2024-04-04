from django.contrib import admin

from basket.models import UserBasket, Basket


# Register your models here.
@admin.register(UserBasket)
class UserBasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'basket', 'product', 'quantity')
    ordering = ('id', 'basket', 'product', 'quantity')
    search_fields = ('product__title', 'basket__user__username')


class ProductInline(admin.TabularInline):
    model = UserBasket


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user',)
    ordering = ('user',)
    search_fields = ('user__username',)
    inlines = [ProductInline]