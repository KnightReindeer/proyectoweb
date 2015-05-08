from django.contrib import admin
from .models import Alumno, Personal, Grupo, Boleta, Tarea, Tutor
# Register your models here.
class PersonalAdmin(admin.ModelAdmin):
	list_display = ('rfc', 'usuario','nombre','fechanacimiento','cargo') 
	list_filter = ('rfc',)

admin.site.register(Tutor)
admin.site.register(Alumno)
admin.site.register(Personal, PersonalAdmin)
admin.site.register(Grupo)
admin.site.register(Boleta)
admin.site.register(Tarea)


