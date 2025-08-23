from django.shortcuts import render , get_object_or_404
from django.http import httpResponSeserverError



def main_points(request):
    points = [
        "fast and affordable",
        "24/7 customer support",
        "wide range of options"
    ]
    return render(request, "main_points.html", {"points":points})
def home(request):
    context = {
        "restaurant_name": settings.RESTAURANT_NAME,
        "restaurant_00": settings.RESTAURANT_PHONE,
    }    
    return render(request, "home.html", context)