from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,TemplateView,ListView,FormView,DeleteView
from .models import Avisos

# Create your views here.
class avisos(ListView):
	template_name = 'pizarron/avisos.html'
	model= Avisos
	context_object_name = 'Avisos'

class crearavisos(CreateView):
	template_name = 'pizarron/crearavisos.html'
	model= Avisos
	success_url= reverse_lazy('avisos')

class eliminaraviso(DeleteView):
	template_name = 'pizarron/eliminaraviso.html'
	model = Avisos
	success_url = reverse_lazy('avisos')


