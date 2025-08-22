from django.urls import path
from .views import *
from .views import home

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
]
