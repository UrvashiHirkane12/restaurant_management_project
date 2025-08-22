from django.shortcuts import render
from django.conf import settings
def home(request):
    context = {
        "restaurant_name": setting.RESTAURANT_NAME
    }
    return render(request, "home.html", context)

def about(request):
    context = {
        "restaurant_name": settings.RESTAURANT_NAME,
        "description": "we are a renowed restaurant",

    } 
   return render(request, "about.html", context) 
# Create your views here.
