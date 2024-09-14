from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# Vistas: es el comportamiento de la página web
# Se crean con funciones "def"                                  # VISTAS BASADAS EN FUNCIONES
# Se hace más sencillo crear vistas basadas en clases "class"   # VISTAS BASADAS EN CLASES

# Es lo mismo, la diferencia radica en qué tan rápido llegas a un resultado.

# CLASES: Está relacionada con programación orientada a objetos.
# Se vincula con la HERENCIA: la clase permite heredar
# Entre paréntesis se incluye de dónde se hereda.

# Paréntesis amarillos = quiere decir que la variable que estamos introduciendo no existe o no la hemos importado.

class HomePageView(TemplateView):

    template_name = "home.html"