# importar una biblioteca administradora de rutas

from django.urls import path

#Importando visitas
from . import views
# Declarando las rutas valdias

urlpatterns = [
    #GET /hello/
    path("", views.index, name="index"),
    #GET /hello/autor
    path("author/", views.author, name="author"),
]
