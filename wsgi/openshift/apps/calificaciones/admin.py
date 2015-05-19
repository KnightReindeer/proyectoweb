from django.contrib import admin
from .models import Alumno, Personal, Grupo, Boleta1, Tarea, Tutor, Escuela
# Register your models here.
class PersonalAdmin(admin.ModelAdmin):
	list_display = ('rfc', 'usuario','nombre','fechanacimiento','cargo') 
	list_filter = ('rfc','nombre','cargo')
	ordering = ('rfc', 'usuario','nombre','fechanacimiento','cargo') 
	search_fields = ('rfc','nombre','fechanacimiento') 

admin.site.register(Tutor)
admin.site.register(Alumno)
admin.site.register(Personal, PersonalAdmin)
admin.site.register(Grupo)
admin.site.register(Boleta1)
admin.site.register(Tarea)
admin.site.register(Escuela)


