from django.shortcuts import render
from django.conf import settings
def home(request):
    context = {
        "restaurant_name": setting.RESTAURANT_NAME
    }
    return render(request, "home.html", context)

# Create your views here.
