from django.shortcuts import render , get_object_or_404
from django.http import HttpResponSeserverError
from .models import reservations, MenuItem
import datetime
from .forms import contactForm
from django.conf import settings
from .models import Restaurant
from .forms import contactForm

def reservation_detail(request , reservation_id):
    try:
        reservation = Reservation.object.get(id=reservation_id)
        return render(request, 'reservation.html', {'reservation':reservation})
    
    except Reservation.DoesNotExist:
        return render(request, '404.html',status=404)
    except Exception as e:
        return HttpResponseServerError("an expected error occured please try again later")    


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


def current_year(request):
    return {'current_year': datetime.datetime.now().year}
    
def home(request):
    if request.method == "POST":
        form = contactForm(request.POST)

        if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form= contactForm()
    return render(request, 'home.html', {'form': form})    

def menu_view(request):
    items = MenuItem.objects.all()
    return render(request, "menu.html", {"items":items})    

def home(request):
    restaurant = Restaurant.objects.first()
    return render(request, "home.html", {"restaurant": restaurant})    

def contact_view(request):
    if request.method == "POST":
        form = ConatctForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact') 
        else:
            form = ContactForm()
            return render(request, 'contact.html',{'form': form})       