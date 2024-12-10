from django.contrib import admin

from .models import Assortment, News, Order, OrderItem

admin.site.register(Assortment)
admin.site.register(News)
admin.site.register(Order)
admin.site.register(OrderItem)
