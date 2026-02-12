from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fruits/', views.fruits, name='fruits'),
    path('filtres/', views.filtres, name='filtres'),
    
    # héritage (nouvelle partie)
    path('heritage/page1/', views.heritage_page1, name='heritage_page1'),
    path('heritage/page2/', views.heritage_page2, name='heritage_page2'),
    
    path('ajax/', views.page_ajax, name='page_ajax'),
    path('ajax/verifier-nom/', views.verifier_nom, name='verifier_nom'),
    path('ajax/formulaire/', views.formulaire_ajax, name='formulaire_ajax'),
    path('ajax/formulaire-post/', views.verifier_formulaire, name='verifier_formulaire'),
    
    # static et media files tests
    path('test-static/', views.test_static_view, name='test_static'),
    path('test-media/', views.test_media_view, name='test_media'),
]
