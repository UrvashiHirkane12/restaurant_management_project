from django.contrib import admin
from .models import userprofile 
from .models import Menu, Order
from .models import MenuItem

admin.site.register(userprofile)
admin.site.register(MenuItem)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "privce")
    search_field = ("name")