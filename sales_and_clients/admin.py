from django.contrib import admin

from .models import  Order,  Client, ShippingAddress

# Register your models here.

# admin.site.register(CartItem)
admin.site.register(Order)
# admin.site.register(Cart)
admin.site.register(Client)
admin.site.register(ShippingAddress)
