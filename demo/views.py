from urllib import request
from django.shortcuts import render
from datetime import date

def home(request):
    context = {
        'title': 'Home Page', 
        'message': 'Welcome to the Home Page!',
        'fruits': ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    }
    return render(request, 'home.html', context)

def fruits(request):
    fruits_list = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

    context = {
        'title': 'Fruits Page',
        'message': 'Here is a list of fruits.',
        'fruits': fruits_list
    }

    return render(request, 'fruits.html', context)
def filtres(request):
    contexte = {
        "nom": "django framework",
        "phrase": "bonjour tout le monde",
        "texte": "Django est un framework web puissant et sécurisé",
        "fruits": ["Pomme", "Banane", "Orange"],
        "prix": 100,
        "note": 14.5678,
        "date": date.today(),
        "actif": True,
        "contenu_html": "<strong>Texte HTML autorisé</strong>",
        "vide": None,
    }
    return render(request, "filtres.html", contexte)

def heritage_page1(request):
    return render(request, 'heritage/page1.html')

def heritage_page2(request):
    contexte = {
        "items": ["Django", "Templates", "Héritage"]
    }
    return render(request, 'heritage/page2.html', contexte)