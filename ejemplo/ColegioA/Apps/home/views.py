from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'

class AdministradoresView(TemplateView):
    template_name='administradores.html'

class EstudiantesView(TemplateView):
    template_name='estudiantes.html'