from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  Tutor, Grupo

class UserForm(UserCreationForm):
	nombre = forms.CharField(label = "NOMBRE")
	apellidop = forms.CharField(label = "APELLIDO PATERNO")
	apellidom = forms.CharField(label = "APELLIDO MATERNO")
	clavepresupuestal = forms.CharField(label = "CLAVE PRESUPUESTAL")
	telefono = forms.CharField(label = "TELEFONO")
	direccion = forms.CharField(label = "DIRECCION")
	correo = forms.CharField(label = "CORREO")
	curp = forms.CharField(label = "CURP")
	aingresep = forms.CharField(label="FECHA DE INGRESO A LA SEP")
	aingreescuela = forms.CharField(label="FECHA DE INGRESO A LA ESCUELA")
	aingrezona = forms.CharField(label="FECHA DE INGRESO A LA ZONA")
	fechanacimiento = forms.DateField(label="FECHA DE NACIMIENTO")
	rfc = forms.CharField(label = "RFC")
	cargo = forms.CharField(label = "CARGO")

class UseraForm(UserCreationForm):
	nombrea = forms.CharField(label = "NOMBRE")
	apellidoPa = forms.CharField(label = "APELLIDO PATERNO")
	apellidoMa = forms.CharField(label = "APELLIDO MATERNO")
	sexo = forms.CharField(label = "SEXO")
	correo = forms.CharField(label = "CORREO")
	curp = forms.CharField(label = "CURP")
	fechanacimiento = forms.DateField(label="FECHA DE NACIMIENTO")
	rh = forms.CharField(label = "Rh")
	tutor1 = forms.ModelChoiceField(queryset= Tutor.objects.all())
	idgrupo = forms.ModelChoiceField(queryset= Grupo.objects.all())


	
