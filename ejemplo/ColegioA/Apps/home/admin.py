from django.contrib import admin
from .models import Comentario, Estudiante,Curso,Telefono,EstudianteB,Art,Comentario,Administrador

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Telefono)
admin.site.register(EstudianteB)
admin.site.register(Art)
admin.site.register(Comentario)
admin.site.register(Administrador)
