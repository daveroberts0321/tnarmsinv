from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Inventory, Orders, Consumables, Supplier, AvailableInventory




# Register your models here.
admin.site.register(Inventory)
admin.site.register(Orders)
admin.site.register(Consumables)
admin.site.register(Supplier)
admin.site.register(AvailableInventory)

