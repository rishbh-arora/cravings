from django.contrib import admin
from .models import CustomUser, menu, order, cart

admin.site.register(CustomUser)
admin.site.register(menu)
admin.site.register(order)
admin.site.register(cart)
