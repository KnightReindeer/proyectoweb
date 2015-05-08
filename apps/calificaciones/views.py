from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView,FormView
from .models import Boleta, Tarea, Personal
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import UserForm 

# Create your views here.
#@login_required()
class registrarcalificaciones (CreateView):
	template_name = 'calificaciones/registrarcalificaciones.html'
	model= Boleta
	success_url= reverse_lazy('calificaciones') #una vez que se ha registrado el 
								#formulario en la bd decide a donde 
								#te mandara

class registrarpersonal(FormView):
	template_name = 'calificaciones/registrarpersonal.html'
	form_class = UserForm
	success_url= reverse_lazy('personal') 

	def form_valid(self, form):
		perfil = Personal()
		perfil.nombre = form.cleaned_data['nombre']
		perfil.apellidop = form.cleaned_data['apellidop']
		perfil.apellidom = form.cleaned_data['apellidom']
		perfil.clavepresupuestal = form.cleaned_data['clavepresupuestal']
		perfil.telefono = form.cleaned_data['telefono']
		perfil.direccion = form.cleaned_data['direccion']
		perfil.correo = form.cleaned_data['correo']
		perfil.curp = form.cleaned_data['curp']
		perfil.aingresep = form.cleaned_data['aingresep']
		perfil.aingreescuela = form.cleaned_data['aingreescuela']
		perfil.aingrezona = form.cleaned_data['aingrezona']
		perfil.fechanacimiento = form.cleaned_data['fechanacimiento']
		perfil.rfc = form.cleaned_data['rfc']
		perfil.cargo = form.cleaned_data['cargo']

		user = form.save()
		perfil.usuario  = user
  		perfil.save()
		return super(registrarpersonal, self).form_valid(form)




#@login_required()
class calificaciones(ListView):
	template_name = 'calificaciones/calificaciones.html'
	model= Boleta
	context_object_name = 'calificaciones'
####aqui mismose pueden crear la cantida de vistas que uno quiera


class personal(ListView):
	template_name = 'calificaciones/personal.html'
	model= Personal
	context_object_name = 'personal'

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
