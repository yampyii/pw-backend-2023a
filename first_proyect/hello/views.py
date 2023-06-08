from django.shortcuts import render
# se importa HttpResponce
from django.http import HttpResponse

#create your views here.
def index(request):
    return HttpResponse("Hola desde mi primer vista 🎹")

def index(request):
    
