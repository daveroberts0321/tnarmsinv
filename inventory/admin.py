from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Inventory




# Register your models here.
admin.site.register(Inventory)
