from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import TemplateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
class index(TemplateView):
	template_name = 'inicio/index.html'

class reglamento(TemplateView):
	template_name = 'inicio/reglamento.html'

class estructura(TemplateView):
	template_name = 'inicio/jerarquia.html'


class Login(TemplateView):
	template_name = 'inicio/login.html'
	#model= Perfiles
	success_url= reverse_lazy('index') 
