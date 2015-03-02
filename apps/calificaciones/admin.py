from django.contrib import admin
from .models import Alumno, Profesor, Grupo, Boleta, Tarea
# Register your models here.

admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Grupo)
admin.site.register(Boleta)
admin.site.register(Tarea)


