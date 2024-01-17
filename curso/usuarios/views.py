from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hola mundo desde usuarios")

def borrar(request):
    return HttpResponse("Borrar usuario")

def calcula_suma(request):
    suma = 2 + 2
    return HttpResponse(f"La suma es {suma}")