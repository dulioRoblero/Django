from django import forms
from .models import Estudiante, Administrador, Curso, Telefono, EstudianteB

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = '__all__'
class EstudiantebForm(forms.ModelForm):
    class Meta:
        model = EstudianteB
        fields = '__all__'

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = '__all__'