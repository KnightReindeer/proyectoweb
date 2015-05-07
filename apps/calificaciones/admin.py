from django.contrib import admin
from .models import Alumno, Personal, Grupo, Boleta, Tarea, Tutor
# Register your models here.

admin.site.register(Tutor)
admin.site.register(Alumno)
admin.site.register(Personal)
admin.site.register(Grupo)
admin.site.register(Boleta)
admin.site.register(Tarea)


