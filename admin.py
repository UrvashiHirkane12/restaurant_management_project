from django.contrib import admin
from .models import userprofile 
from .models import Menu, Order

admin.site.register(userprofile)

class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "privce")
    search_field = ("name")