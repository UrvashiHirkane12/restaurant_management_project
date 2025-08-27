from django.urls import path
from . import views
urlpatterns = [
    path('feedback/', views.feedback_view, name='feedback'),
    path('feedback/thanks/', views.feedback_thanks, name='feedback_thanks'),
    path('', views.home, name='home'),
    path("menu/", views.menu_view, name="menu"),
]