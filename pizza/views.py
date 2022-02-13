from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

def calosc (request):
    wszystkie = Pizza.objects.all()
    return render(request, 'pizza.html', {"pizza": wszystkie})


def wyswietl (request):
    return render(request, 'wyswietl.html')

def finalizacja (request):
    return render(request, 'gratulacje.html')
