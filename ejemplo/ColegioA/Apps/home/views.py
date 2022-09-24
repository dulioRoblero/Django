from audioop import reverse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView 
from .forms import EstudianteForm, AdministradorForm, EstudiantebForm,CursoForm,TelefonoForm
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'

class AdministradoresView(TemplateView):
    template_name='administradores.html'

class EstudiantesView(TemplateView):
    template_name='estudiantes.html'

class CrearEstudiantesView(CreateView):
        template_namem = 'crear.html'
        form_class = EstudianteForm 
        success_url = reverse_lazy('home:homeapp')


class CrearAdministradorView(CreateView):
        template_namem = 'crear1.html'
        form_class = AdministradorForm
        success_url = reverse_lazy('home:homeapp')

class CrearCursoView(CreateView):
        template_namem = 'crear2.html'
        form_class = CursoForm 
        success_url = reverse_lazy('home:homeapp')

class CrearTelefonoView(CreateView):
        template_namem = 'crea3r.html'
        form_class = TelefonoForm
        success_url = reverse_lazy('home:homeapp')

