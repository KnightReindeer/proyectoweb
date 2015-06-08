from django.contrib import admin
from .models import Alumno, Personal, Grupo, Boleta1, Tarea, Tutor, Escuela, Boleta2, Boleta3, Boleta4, Boleta5, Boleta6
# Register your models here.
class PersonalAdmin(admin.ModelAdmin):
	list_display = ('rfc', 'usuario','nombre','fechanacimiento','cargo') 
	list_filter = ('rfc','nombre','cargo')
	ordering = ('rfc', 'usuario','nombre','fechanacimiento','cargo') 
	search_fields = ('rfc','nombre','fechanacimiento') 

class TareaAdmin(admin.ModelAdmin):
	list_display = ('fechatarea','fechapublica','titulo') 
	list_filter = ('fechatarea','fechapublica','titulo')
	ordering = ('fechatarea','fechapublica','titulo') 
	search_fields = ('fechatarea','tarea','fechapublica','titulo') 


admin.site.register(Tutor)
admin.site.register(Alumno)
admin.site.register(Personal, PersonalAdmin)
admin.site.register(Grupo)
admin.site.register(Boleta1)
admin.site.register(Boleta2)
admin.site.register(Boleta3)
admin.site.register(Boleta4)
admin.site.register(Boleta5)
admin.site.register(Boleta6)
admin.site.register(Tarea, TareaAdmin)
admin.site.register(Escuela)


