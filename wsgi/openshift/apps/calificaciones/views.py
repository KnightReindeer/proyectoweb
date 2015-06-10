from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView,FormView,UpdateView, DeleteView
from .models import Boleta1,Boleta2,Boleta3,Boleta4,Boleta5,Boleta6, Tarea, Personal, Alumno, Tutor, Grupo
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required 
from django.views.generic.base import TemplateResponseMixin
from .forms import UserForm,UseraForm 
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
# Create your views here.
#@login_required()
class registrarcalificaciones (CreateView):
	template_name = 'calificaciones/registrarcalificaciones.html'
	model= Boleta1
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


class registraralumno(FormView):
	template_name = 'calificaciones/registraralumnos.html'
	form_class = UseraForm
	success_url= reverse_lazy('alumno') 

	def form_valid(self, form):
		perfila = Alumno()
		perfila.nombrea = form.cleaned_data['nombrea']
		perfila.apellidoPa = form.cleaned_data['apellidoPa']
		perfila.apellidoMa = form.cleaned_data['apellidoMa']
		perfila.sexo = form.cleaned_data['sexo']
		perfila.correo = form.cleaned_data['correo']
		perfila.curp = form.cleaned_data['curp']
		perfila.fechanacimiento = form.cleaned_data['fechanacimiento']
		perfila.rh = form.cleaned_data['rh']
		perfila.tutor1 = form.cleaned_data['tutor1']
		perfila.idgrupo = form.cleaned_data['idgrupo']
		usera = form.save()
		perfila.usuario  = usera
  		perfila.save()
		return super(registraralumno, self).form_valid(form)


class registrartutor (CreateView):
	template_name = 'calificaciones/registrartutor.html'
	model= Tutor
	success_url= reverse_lazy('registraralumno')

class tutor(ListView):
	template_name = 'calificaciones/tutor.html'
	model= Tutor
	context_object_name = 'tutores'

class registrargrupo(CreateView):
	template_name = 'calificaciones/registrargrupo.html'
	model= Grupo
	success_url= reverse_lazy('grupo')

class grupo(ListView):
	template_name = 'calificaciones/grupo.html'
	model= Grupo
	context_object_name = 'grupos'

class calificaciones(UpdateView):
	model= Boleta1
	context_object_name = 'calificaciones'
	template_name = 'calificaciones/calificaciones.html'
	#form_class = Boleta1Form
	success_url = '/vercalificaciones/'

class calificaciones2(UpdateView):
	model= Boleta2
	context_object_name = 'calificaciones'
	template_name = 'calificaciones/calificaciones2.html'
	#form_class = Boleta1Form
	success_url = '/vercalificaciones2/'

class calificaciones3(UpdateView):
	model= Boleta3
	context_object_name = 'calificaciones'
	template_name = 'calificaciones/calificaciones3.html'
	#form_class = Boleta1Form
	success_url = '/vercalificaciones3/'

class calificaciones4(UpdateView):
	model= Boleta4
	context_object_name = 'calificaciones'
	template_name = 'calificaciones/calificaciones4.html'
	#form_class = Boleta1Form
	success_url = '/vercalificaciones4/'

class calificaciones5(UpdateView):
	model= Boleta5
	context_object_name = 'calificaciones'
	template_name = 'calificaciones/calificaciones5.html'
	#form_class = Boleta1Form
	success_url = '/vercalificaciones5/'

class calificaciones6(UpdateView):
	model= Boleta6
	context_object_name = 'calificaciones'
	template_name = 'calificaciones/calificaciones6.html'
	#form_class = Boleta1Form
	success_url = '/vercalificaciones6/'

class vercalificaciones(ListView):
	template_name = 'calificaciones/vercalificaciones.html'
	context_object_name = 'calificaciones'

	def get_queryset(self):
		consulta1=Boleta1.objects.filter(idgrupo__idprofesor__usuario__username=self.request.user, idprofesor__usuario__username=self.request.user).order_by("idalumno")
		consulta2=Boleta1.objects.filter(idgrupo__alumno__usuario__username=self.request.user, idalumno__usuario__username=self.request.user)
		if consulta1:
			return consulta1
		elif consulta2:
			return consulta2
		#else:
		#	return Boleta1.objects.all().order_by("idgrupo")

	def get_context_data(self, **kwargs):
		context = super(vercalificaciones, self).get_context_data(**kwargs)
		#context['now'] = "hola variables!!!"
		return context

class vercalificaciones2(ListView):
	template_name = 'calificaciones/vercalificaciones2.html'
	context_object_name = 'calificaciones'

	def get_queryset(self):
		consulta1=Boleta2.objects.filter(idgrupo__idprofesor__usuario__username=self.request.user, idprofesor__usuario__username=self.request.user).order_by("idalumno")
		consulta2=Boleta2.objects.filter(idgrupo__alumno__usuario__username=self.request.user, idalumno__usuario__username=self.request.user)
		if consulta1:
			return consulta1
		elif consulta2:
			return consulta2
		#else:
		#	return Boleta1.objects.all().order_by("idgrupo")

	def get_context_data(self, **kwargs):
		context = super(vercalificaciones2, self).get_context_data(**kwargs)
		#context['now'] = "hola variables!!!"
		return context

class vercalificaciones3(ListView):
	template_name = 'calificaciones/vercalificaciones3.html'
	context_object_name = 'calificaciones'

	def get_queryset(self):
		consulta1=Boleta3.objects.filter(idgrupo__idprofesor__usuario__username=self.request.user, idprofesor__usuario__username=self.request.user).order_by("idalumno")
		consulta2=Boleta3.objects.filter(idgrupo__alumno__usuario__username=self.request.user, idalumno__usuario__username=self.request.user)
		if consulta1:
			return consulta1
		elif consulta2:
			return consulta2
		#else:
		#	return Boleta1.objects.all().order_by("idgrupo")

	def get_context_data(self, **kwargs):
		context = super(vercalificaciones3, self).get_context_data(**kwargs)
		#context['now'] = "hola variables!!!"
		return context

class vercalificaciones4(ListView):
	template_name = 'calificaciones/vercalificaciones4.html'
	context_object_name = 'calificaciones'

	def get_queryset(self):
		consulta1=Boleta4.objects.filter(idgrupo__idprofesor__usuario__username=self.request.user, idprofesor__usuario__username=self.request.user).order_by("idalumno")
		consulta2=Boleta4.objects.filter(idgrupo__alumno__usuario__username=self.request.user, idalumno__usuario__username=self.request.user)
		if consulta1:
			return consulta1
		elif consulta2:
			return consulta2
		#else:
		#	return Boleta1.objects.all().order_by("idgrupo")

	def get_context_data(self, **kwargs):
		context = super(vercalificaciones4, self).get_context_data(**kwargs)
		#context['now'] = "hola variables!!!"
		return context

class vercalificaciones5(ListView):
	template_name = 'calificaciones/vercalificaciones5.html'
	context_object_name = 'calificaciones'

	def get_queryset(self):
		consulta1=Boleta5.objects.filter(idgrupo__idprofesor__usuario__username=self.request.user, idprofesor__usuario__username=self.request.user).order_by("idalumno")
		consulta2=Boleta5.objects.filter(idgrupo__alumno__usuario__username=self.request.user, idalumno__usuario__username=self.request.user)
		if consulta1:
			return consulta1
		elif consulta2:
			return consulta2
		#else:
		#	return Boleta1.objects.all().order_by("idgrupo")

	def get_context_data(self, **kwargs):
		context = super(vercalificaciones5, self).get_context_data(**kwargs)
		#context['now'] = "hola variables!!!"
		return context

class vercalificaciones6(ListView):
	template_name = 'calificaciones/vercalificaciones6.html'
	context_object_name = 'calificaciones'

	def get_queryset(self):
		consulta1=Boleta6.objects.filter(idgrupo__idprofesor__usuario__username=self.request.user, idprofesor__usuario__username=self.request.user).order_by("idalumno")
		consulta2=Boleta6.objects.filter(idgrupo__alumno__usuario__username=self.request.user, idalumno__usuario__username=self.request.user)
		if consulta1:
			return consulta1
		elif consulta2:
			return consulta2
		#else:
		#	return Boleta1.objects.all().order_by("idgrupo")

	def get_context_data(self, **kwargs):
		context = super(vercalificaciones6, self).get_context_data(**kwargs)
		#context['now'] = "hola variables!!!"
		return context

class alumno(ListView):
	template_name = 'calificaciones/alumnos.html'
	context_object_name = 'alumnos'

	def get_queryset(self):
		consulta1=Alumno.objects.filter(idgrupo__idprofesor__usuario__username=self.request.user).order_by("nombrea")
		if consulta1:
			return consulta1
		else:
			return Alumno.objects.all().order_by("idgrupo")

	def get_context_data(self, **kwargs):
		context = super(alumno, self).get_context_data(**kwargs)
		#context['now'] = "hola variables!!!"
		return context




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
	context_object_name = 'tareas'
	def get_queryset(self):
		query2=Tarea.objects.filter(idgrupo__idprofesor__usuario__username=self.request.user)
		query=Tarea.objects.filter(idgrupo__alumno__usuario__username=self.request.user)
		if query:
			return query 
		if query2:
			return query2
		else:
			return Tarea.objects.all

class eliminartarea(DeleteView):
	template_name = 'calificaciones/eliminartarea.html'
	model = Tarea
	success_url = reverse_lazy('tareas')


