from django.conf import settings
from django.http import JsonResponse
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

def page_ajax(request):
    return render(request, 'ajax/ajax.html')

def verifier_nom(request):
    nom = request.GET.get('nom', '').strip()
    if nom=="":
        return JsonResponse({
            "valide":False,
            "message":"Le nom ne peut pas être vide."
        })
    if len(nom) < 3:
        return JsonResponse({
            "valide": False,
            "message":"Le nom doit contenir au moins 3 caractères."
        })
    return JsonResponse({ "valide": True, "message":"Le nom est valide." })

# page formulaire
def formulaire_ajax(request):
    return render(request, "ajax/formulaire_ajax.html")

# traitement AJAX POST
def verifier_formulaire(request):
    if request.method == "POST":
        nom = request.POST.get("nom", "").strip()
        email = request.POST.get("email", "").strip()
        if not nom or not email:
            return JsonResponse({
                "valide": False,
                "message": "Tous les champs sont obligatoires !"
            })
        if len(nom) < 3:
            return JsonResponse({
                "valide": False,
                "message": "Nom trop court !"
            })
        if "@" not in email:
            return JsonResponse({
                "valide": False,
                "message": "Email invalide !"
            })
        return JsonResponse({
            "valide": True,
            "message": f"Bonjour {nom}, votre email {email} est valide !"
        })
    else:
        return JsonResponse({
            "valide": False,
            "message": "Requête invalide"
        })

def test_static_view(request):
    return render(request, 'demo/test_static.html')

def test_media_view(request):
    uploaded_file_url = settings.MEDIA_URL + 'photo.svg'
    return render(request, 'demo/test_media.html', {'file_url': uploaded_file_url})