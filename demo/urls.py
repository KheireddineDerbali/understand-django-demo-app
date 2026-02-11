from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fruits/', views.fruits, name='fruits'),
]