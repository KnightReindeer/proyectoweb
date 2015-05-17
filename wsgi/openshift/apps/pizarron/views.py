from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView, FormView

# Create your views here.
class avisos(TemplateView):
	template_name = 'pizarron/avisos.html'

class crearavisos(TemplateView):
	template_name = 'pizarron/crearavisos.html'




