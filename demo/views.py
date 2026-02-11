from django.shortcuts import render

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