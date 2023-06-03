from django.contrib import admin
from .models import CustomUser, menu, order

admin.site.register(CustomUser)
admin.site.register(menu)
admin.site.register(order)
