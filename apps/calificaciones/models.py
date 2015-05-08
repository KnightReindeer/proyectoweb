from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Personal(models.Model):
	usuario = models.OneToOneField(User)
	nombre = models.CharField(max_length=50, blank=True)
	apellidop = models.CharField(max_length=50, blank=True)
	apellidom = models.CharField(max_length=50, blank=True)
	clavepresupuestal = models.CharField(max_length=50, blank=True)
	telefono = models.CharField(max_length=13, blank=True)
	direccion = models.CharField(max_length=80, blank=True)
	correo = models.CharField(max_length=20, blank=True)
	curp = models.CharField(max_length=50, blank=True)
	aingresep = models.CharField(max_length=6, blank=True)
	aingreescuela = models.CharField(max_length=6, blank=True)
	aingrezona = models.CharField(max_length=6, blank=True)
	fechanacimiento = models.DateField(blank=True, null=True)
	rfc = models.CharField(max_length=50, blank=True)
	cargo = models.CharField(max_length=50, blank=True)
	
	def __unicode__(self):
		return self.rfc

class Tutor(models.Model):
	idT= models.CharField(max_length=50, blank=True)
	nombreT = models.CharField(max_length=50, blank=True)
	apellidoPt = models.CharField(max_length=50, blank=True)
	apellidoMt= models.CharField(max_length=50, blank=True)
	ocupacion= models.CharField(max_length=50, blank=True)
	direccion= models.CharField(max_length=50, blank=True)
	telefonoCasa= models.CharField(max_length=50, blank=True)
	telefonoCel= models.CharField(max_length=50, blank=True)
	def __unicode__(self):
		return self.idT


class Alumno(models.Model):
	nombrea = models.CharField(max_length=50, blank=True)
	apellidoPa = models.CharField(max_length=50, blank=True)
	apellidoMa= models.CharField(max_length=50, blank=True)
	curp = models.CharField(max_length=45, blank=True)
	fechanacimiento = models.DateField(blank=True, null=True)
	rh = models.CharField(max_length=50, blank=True) #tipo sangre
	tutor1= models.ForeignKey(Tutor)
	def __unicode__(self):
		return self.curp

class Grupo(models.Model):
	gradogrupo = models.CharField(max_length=10, blank=True) #se ingresa  2 A , 3C, ETC
	idprofesor = models.ForeignKey(Personal)
	idalumno = models.ForeignKey(Alumno)
	def __unicode__(self):
		return self.gradogrupo


class Boleta(models.Model):
	codigoboleta= models.CharField(max_length=50, blank=True)
	idprofesor=  models.ForeignKey(Personal)
	idalumno = models.ForeignKey(Alumno)
	def __unicode__(self):
		return self.codigoboleta

class Tarea(models.Model):
	idgrupo=  models.ForeignKey(Grupo)
	tarea = models.TextField(max_length=200, blank=True)	
	#def __unicode__(self):
	#	return self.idgrupo
class Consejo(models.Model):
	director=  models.ForeignKey(Personal)
	#profesor=  models.ForeignKey(Personal)
	