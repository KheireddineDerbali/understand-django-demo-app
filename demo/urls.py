from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fruits/', views.fruits, name='fruits'),
    path('filtres/', views.filtres, name='filtres'),
    
    # héritage (nouvelle partie)
    path('heritage/page1/', views.heritage_page1, name='heritage_page1'),
    path('heritage/page2/', views.heritage_page2, name='heritage_page2'),
]