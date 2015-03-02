from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView
from .models import Boleta, Tarea
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
class registrarcalificaciones (CreateView):
	template_name = 'calificaciones/registrarcalificaciones.html'
	model= Boleta
	success_url= reverse_lazy('calificaciones') #una vez que se ha registrado el 
								#formulario en la bd decide a donde 
								#te mandara

class calificaciones(ListView):
	template_name = 'calificaciones/calificaciones.html'
	model= Boleta
	context_object_name = 'calificaciones'
####aqui mismose pueden crear la cantida de vistas que uno quiera


class creartareas (CreateView):
	template_name = 'calificaciones/registrartareas.html'
	model= Tarea
	success_url= reverse_lazy('tareas') #una vez que se ha registrado el 
								#formulario en la bd decide a donde 
								#te mandara

class tareas(ListView):
	template_name = 'calificaciones/tareas.html'
	model= Tarea
	context_object_name = 'tareas'
