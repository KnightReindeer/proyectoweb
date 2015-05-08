from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
	nombre = forms.CharField(label = "NOMBRE COMPLETO")
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
	

	
