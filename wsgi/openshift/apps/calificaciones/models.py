from django.db import models
from django.contrib.auth.models import User
from datetime import datetime    
from django.forms import ModelForm
from django import forms
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
	rfc = models.CharField(max_length=50, blank=True, null=True)
	cargo = models.CharField(max_length=50, blank=True, null=True, default="PROFESOR")
	
	def __unicode__(self):
		return self.rfc

class Tutor(models.Model):
	nombreT = models.CharField(max_length=50, blank=True)
	apellidoPt = models.CharField(max_length=50, blank=True)
	apellidoMt= models.CharField(max_length=50, blank=True)
	ocupacion= models.CharField(max_length=50, blank=True)
	direccion= models.CharField(max_length=50, blank=True)
	telefonoCasa= models.CharField(max_length=50, null=True, blank=True)
	telefonoCel= models.CharField(max_length=50, null=True, blank=True)
	def __unicode__(self):
		return unicode(self.apellidoPt)+ ' ' + str(self.apellidoMt)+ ' ' + str(self.nombreT)


class Grupo(models.Model):
	gradogrupo = models.CharField(max_length=10, blank=True) #se ingresa  2 A , 3C, ETC
	idprofesor = models.ForeignKey(Personal)
	def __unicode__(self):
		return self.gradogrupo


class Alumno(models.Model):
	usuario = models.OneToOneField(User)
	nombrea = models.CharField(max_length=50, blank=True)
	apellidoPa = models.CharField(max_length=50, blank=True)
	apellidoMa= models.CharField(max_length=50, blank=True)
	sexo = models.CharField(max_length=15, blank=True)
	correo = models.CharField(max_length=30, blank=True)
	curp = models.CharField(max_length=45, blank=True)
	fechanacimiento = models.DateField(blank=True, null=True)
	rh = models.CharField(max_length=50, blank=True) #tipo sangre
	tutor1= models.ForeignKey(Tutor)
	idgrupo = models.ForeignKey(Grupo)
	def __unicode__(self):
		return unicode(self.apellidoPa)+ ' ' + str(self.apellidoMa)+ ' ' + str(self.nombrea)+ ' ' + str(self.curp)

	class Meta:
		permissions = (
            ("ver_alumno", "Permiso para visualizar los datos de alumnos"),
        )


class Escuela(models.Model):
	clave= models.CharField(max_length=12, blank=True)
	nombre=  models.CharField(max_length=50, blank=True)
	zona = models.CharField(max_length=50, blank=True)
	turno=  models.CharField(max_length=12, blank=True)
	direccion = models.CharField(max_length=50, blank=True)
	telefono = models.CharField(max_length=15, blank=True)
	correo = models.CharField(max_length=50, blank=True)
	paginaweb = models.CharField(max_length=50, blank=True)

	def __unicode__(self):
		return unicode(self.nombre)+ ' ' + str(self.turno)+ ' ' + str(self.clave)


class Boleta1(models.Model):
	codigoboleta = models.CharField(max_length=50, blank=True)
	idprofesor=  models.ForeignKey(Personal)
	idgrupo =  models.ForeignKey(Grupo)
	idalumno = models.ForeignKey(Alumno)
	idescuela = models.ForeignKey(Escuela)
	cicloescolar = models.CharField(max_length=50, blank=True, null=True)
	fechadevalidacion = models.DateField(default=datetime.now, blank=True, null=True, )
	lugardevalidacion =models.CharField(default="-", max_length=50, blank=True, null=True)
	promovido = models.BooleanField(default=False)
	promedio = models.DecimalField(max_digits = 3, decimal_places = 1,default=0.0, blank=True, null=True)
	inasistencias1= models.IntegerField(default=0, blank=True, null=True)
	inasistencias2= models.IntegerField(default=0, blank=True, null=True)
	inasistencias3= models.IntegerField(default=0, blank=True, null=True)
	inasistencias4= models.IntegerField(default=0, blank=True, null=True)
	inasistencias5= models.IntegerField(default=0, blank=True, null=True)
	inasistenciastotal= models.IntegerField(default=0, blank=True, null=True)
	espanol1 = models.IntegerField(default=0, blank=True, null=True)
	espanol2 = models.IntegerField(default=0, blank=True, null=True)
	espanol3 = models.IntegerField(default=0, blank=True, null=True)
	espanol4 = models.IntegerField(default=0, blank=True, null=True)
	espanol5 = models.IntegerField(default=0, blank=True, null=True)
	espanolpromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	matematicas1 = models.IntegerField(default=0, blank=True, null=True)
	matematicas2 = models.IntegerField(default=0, blank=True, null=True)
	matematicas3 = models.IntegerField(default=0, blank=True, null=True)
	matematicas4 = models.IntegerField(default=0, blank=True, null=True)
	matematicas5 = models.IntegerField(default=0, blank=True, null=True)
	matematicaspromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	exploracion1 = models.IntegerField(default=0, blank=True, null=True)
	exploracion2 = models.IntegerField(default=0, blank=True, null=True)
	exploracion3 = models.IntegerField(default=0, blank=True, null=True)
	exploracion4 = models.IntegerField(default=0, blank=True, null=True)
	exploracion5 = models.IntegerField(default=0, blank=True, null=True)
	exploracionpromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	formacion1 = models.IntegerField(default=0, blank=True, null=True)
	formacion2 = models.IntegerField(default=0, blank=True, null=True)
	formacion3 = models.IntegerField(default=0, blank=True, null=True)
	formacion4 = models.IntegerField(default=0, blank=True, null=True)
	formacion5 = models.IntegerField(default=0, blank=True, null=True)
	formacionpromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	fisica1 = models.IntegerField(default=0, blank=True, null=True)
	fisica2 = models.IntegerField(default=0, blank=True, null=True)
	fisica3 = models.IntegerField(default=0, blank=True, null=True)
	fisica4 = models.IntegerField(default=0, blank=True, null=True)
	fisica5 = models.IntegerField(default=0, blank=True, null=True)
	fisicapromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	artistica1 = models.IntegerField(default=0, blank=True, null=True)
	artistica2 = models.IntegerField(default=0, blank=True, null=True)
	artistica3 = models.IntegerField(default=0, blank=True, null=True)
	artistica4 = models.IntegerField(default=0, blank=True, null=True)
	artistica5 = models.IntegerField(default=0, blank=True, null=True)
	artisticapromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	aviso1 = models.BooleanField(default=False)
	aviso2 = models.BooleanField(default=False)
	aviso3 = models.BooleanField(default=False)

	def inasistenciastotal1 (self):
		inatotal1=self.inasistencias1+self.inasistencias2+self.inasistencias3+self.inasistencias4+self.inasistencias5      
		return inatotal1

	def espanolpromedio1 (self):
		espapromedio1=self.espanol1+self.espanol2+self.espanol3+self.espanol4+self.espanol5
		return str(espapromedio1)

	def matemapromedio1 (self):
		matepromedio1=(self.matematicas1+self.matematicas2+self.matematicas3+self.matematicas4+self.ematematicas5)/5
		return matepromedio1

	def __unicode__(self):
					return self.codigoboleta

	class Meta:
		permissions = (
            ("ver_boleta1", "Permiso para visualizar las boletas de primero"),
        )

class Boleta2(models.Model):
	codigoboleta = models.CharField(max_length=50, blank=True)
	idprofesor=  models.ForeignKey(Personal)
	idgrupo =  models.ForeignKey(Grupo)
	idalumno = models.ForeignKey(Alumno)
	idescuela = models.ForeignKey(Escuela)
	cicloescolar = models.CharField(max_length=50, blank=True, null=True)
	fechadevalidacion = models.DateField(default=datetime.now, blank=True, null=True, )
	lugardevalidacion =models.CharField(default="-", max_length=50, blank=True, null=True)
	promovido = models.BooleanField(default=False)
	promedio = models.DecimalField(max_digits = 3, decimal_places = 1,default=0.0, blank=True, null=True)
	inasistencias1= models.IntegerField(default=0, blank=True, null=True)
	inasistencias2= models.IntegerField(default=0, blank=True, null=True)
	inasistencias3= models.IntegerField(default=0, blank=True, null=True)
	inasistencias4= models.IntegerField(default=0, blank=True, null=True)
	inasistencias5= models.IntegerField(default=0, blank=True, null=True)
	inasistenciastotal= models.IntegerField(default=0, blank=True, null=True)
	espanol1 = models.IntegerField(default=0, blank=True, null=True)
	espanol2 = models.IntegerField(default=0, blank=True, null=True)
	espanol3 = models.IntegerField(default=0, blank=True, null=True)
	espanol4 = models.IntegerField(default=0, blank=True, null=True)
	espanol5 = models.IntegerField(default=0, blank=True, null=True)
	espanolpromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	matematicas1 = models.IntegerField(default=0, blank=True, null=True)
	matematicas2 = models.IntegerField(default=0, blank=True, null=True)
	matematicas3 = models.IntegerField(default=0, blank=True, null=True)
	matematicas4 = models.IntegerField(default=0, blank=True, null=True)
	matematicas5 = models.IntegerField(default=0, blank=True, null=True)
	matematicaspromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	exploracion1 = models.IntegerField(default=0, blank=True, null=True)
	exploracion2 = models.IntegerField(default=0, blank=True, null=True)
	exploracion3 = models.IntegerField(default=0, blank=True, null=True)
	exploracion4 = models.IntegerField(default=0, blank=True, null=True)
	exploracion5 = models.IntegerField(default=0, blank=True, null=True)
	exploracionpromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	formacion1 = models.IntegerField(default=0, blank=True, null=True)
	formacion2 = models.IntegerField(default=0, blank=True, null=True)
	formacion3 = models.IntegerField(default=0, blank=True, null=True)
	formacion4 = models.IntegerField(default=0, blank=True, null=True)
	formacion5 = models.IntegerField(default=0, blank=True, null=True)
	formacionpromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	fisica1 = models.IntegerField(default=0, blank=True, null=True)
	fisica2 = models.IntegerField(default=0, blank=True, null=True)
	fisica3 = models.IntegerField(default=0, blank=True, null=True)
	fisica4 = models.IntegerField(default=0, blank=True, null=True)
	fisica5 = models.IntegerField(default=0, blank=True, null=True)
	fisicapromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	artistica1 = models.IntegerField(default=0, blank=True, null=True)
	artistica2 = models.IntegerField(default=0, blank=True, null=True)
	artistica3 = models.IntegerField(default=0, blank=True, null=True)
	artistica4 = models.IntegerField(default=0, blank=True, null=True)
	artistica5 = models.IntegerField(default=0, blank=True, null=True)
	artisticapromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	aviso1 = models.BooleanField(default=False)
	aviso2 = models.BooleanField(default=False)
	aviso3 = models.BooleanField(default=False)

	def __unicode__(self):
		return self.codigoboleta

	class Meta:
		permissions = (
            ("ver_boleta2", "Permiso para visualizar las boletas de segundo"),
        )

class Boleta3(models.Model):
	codigoboleta = models.CharField(max_length=50, blank=True)
	idprofesor=  models.ForeignKey(Personal)
	idgrupo =  models.ForeignKey(Grupo)
	idalumno = models.ForeignKey(Alumno)
	idescuela = models.ForeignKey(Escuela)
	cicloescolar = models.CharField(max_length=50, blank=True, null=True)
	fechadevalidacion = models.DateField(default=datetime.now, blank=True, null=True, )
	lugardevalidacion =models.CharField(default="-", max_length=50, blank=True, null=True)
	promovido = models.BooleanField(default=False)
	promedio = models.DecimalField(max_digits = 3, decimal_places = 1,default=0.0, blank=True, null=True)
	inasistencias1= models.IntegerField(default=0, blank=True, null=True)
	inasistencias2= models.IntegerField(default=0, blank=True, null=True)
	inasistencias3= models.IntegerField(default=0, blank=True, null=True)
	inasistencias4= models.IntegerField(default=0, blank=True, null=True)
	inasistencias5= models.IntegerField(default=0, blank=True, null=True)
	inasistenciastotal= models.IntegerField(default=0, blank=True, null=True)
	espanol1 = models.IntegerField(default=0, blank=True, null=True)
	espanol2 = models.IntegerField(default=0, blank=True, null=True)
	espanol3 = models.IntegerField(default=0, blank=True, null=True)
	espanol4 = models.IntegerField(default=0, blank=True, null=True)
	espanol5 = models.IntegerField(default=0, blank=True, null=True)
	espanolpromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	ciencias1 = models.IntegerField(default=0, blank=True, null=True)
	ciencias2 = models.IntegerField(default=0, blank=True, null=True)
	ciencias3 = models.IntegerField(default=0, blank=True, null=True)
	ciencias4 = models.IntegerField(default=0, blank=True, null=True)
	ciencias5 = models.IntegerField(default=0, blank=True, null=True)
	cienciaspromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	entidad1 = models.IntegerField(default=0, blank=True, null=True)
	entidad2 = models.IntegerField(default=0, blank=True, null=True)
	entidad3 = models.IntegerField(default=0, blank=True, null=True)
	entidad4 = models.IntegerField(default=0, blank=True, null=True)
	entidad5 = models.IntegerField(default=0, blank=True, null=True)
	entidadpromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	formacion1 = models.IntegerField(default=0, blank=True, null=True)
	formacion2 = models.IntegerField(default=0, blank=True, null=True)
	formacion3 = models.IntegerField(default=0, blank=True, null=True)
	formacion4 = models.IntegerField(default=0, blank=True, null=True)
	formacion5 = models.IntegerField(default=0, blank=True, null=True)
	formacionpromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	fisica1 = models.IntegerField(default=0, blank=True, null=True)
	fisica2 = models.IntegerField(default=0, blank=True, null=True)
	fisica3 = models.IntegerField(default=0, blank=True, null=True)
	fisica4 = models.IntegerField(default=0, blank=True, null=True)
	fisica5 = models.IntegerField(default=0, blank=True, null=True)
	fisicapromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	artistica1 = models.IntegerField(default=0, blank=True, null=True)
	artistica2 = models.IntegerField(default=0, blank=True, null=True)
	artistica3 = models.IntegerField(default=0, blank=True, null=True)
	artistica4 = models.IntegerField(default=0, blank=True, null=True)
	artistica5 = models.IntegerField(default=0, blank=True, null=True)
	artisticapromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	aviso1 = models.BooleanField(default=False)
	aviso2 = models.BooleanField(default=False)
	aviso3 = models.BooleanField(default=False)

	def __unicode__(self):
		return self.codigoboleta

	class Meta:
		permissions = (
            ("ver_boleta3", "Permiso para visualizar las boletas de tercero"),
        )


class Boleta4(models.Model):
	codigoboleta = models.CharField(max_length=50, blank=True)
	idprofesor=  models.ForeignKey(Personal)
	idgrupo =  models.ForeignKey(Grupo)
	idalumno = models.ForeignKey(Alumno)
	idescuela = models.ForeignKey(Escuela)
	cicloescolar = models.CharField(max_length=50, blank=True, null=True)
	fechadevalidacion = models.DateField(default=datetime.now, blank=True, null=True, )
	lugardevalidacion =models.CharField(default="-", max_length=50, blank=True, null=True)
	promovido = models.BooleanField(default=False)
	promedio = models.DecimalField(max_digits = 3, decimal_places = 1,default=0.0, blank=True, null=True)
	inasistencias1= models.IntegerField(default=0, blank=True, null=True)
	inasistencias2= models.IntegerField(default=0, blank=True, null=True)
	inasistencias3= models.IntegerField(default=0, blank=True, null=True)
	inasistencias4= models.IntegerField(default=0, blank=True, null=True)
	inasistencias5= models.IntegerField(default=0, blank=True, null=True)
	inasistenciastotal= models.IntegerField(default=0, blank=True, null=True)
	espanol1 = models.IntegerField(default=0, blank=True, null=True)
	espanol2 = models.IntegerField(default=0, blank=True, null=True)
	espanol3 = models.IntegerField(default=0, blank=True, null=True)
	espanol4 = models.IntegerField(default=0, blank=True, null=True)
	espanol5 = models.IntegerField(default=0, blank=True, null=True)
	espanolpromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	matematicas1 = models.IntegerField(default=0, blank=True, null=True)
	matematicas2 = models.IntegerField(default=0, blank=True, null=True)
	matematicas3 = models.IntegerField(default=0, blank=True, null=True)
	matematicas4 = models.IntegerField(default=0, blank=True, null=True)
	matematicas5 = models.IntegerField(default=0, blank=True, null=True)
	matematicaspromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	ciencias1 = models.IntegerField(default=0, blank=True, null=True)
	ciencias2 = models.IntegerField(default=0, blank=True, null=True)
	ciencias3 = models.IntegerField(default=0, blank=True, null=True)
	ciencias4 = models.IntegerField(default=0, blank=True, null=True)
	ciencias5 = models.IntegerField(default=0, blank=True, null=True)
	cienciaspromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	geografia1 = models.IntegerField(default=0, blank=True, null=True)
	geografia2 = models.IntegerField(default=0, blank=True, null=True)
	geografia3 = models.IntegerField(default=0, blank=True, null=True)
	geografia4 = models.IntegerField(default=0, blank=True, null=True)
	geografia5 = models.IntegerField(default=0, blank=True, null=True)
	geografiapromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	historia1 = models.IntegerField(default=0, blank=True, null=True)
	historia2 = models.IntegerField(default=0, blank=True, null=True)
	historia3 = models.IntegerField(default=0, blank=True, null=True)
	historia4 = models.IntegerField(default=0, blank=True, null=True)
	historia5 = models.IntegerField(default=0, blank=True, null=True)
	historiapromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	formacion1 = models.IntegerField(default=0, blank=True, null=True)
	formacion2 = models.IntegerField(default=0, blank=True, null=True)
	formacion3 = models.IntegerField(default=0, blank=True, null=True)
	formacion4 = models.IntegerField(default=0, blank=True, null=True)
	formacion5 = models.IntegerField(default=0, blank=True, null=True)
	formacionpromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	fisica1 = models.IntegerField(default=0, blank=True, null=True)
	fisica2 = models.IntegerField(default=0, blank=True, null=True)
	fisica3 = models.IntegerField(default=0, blank=True, null=True)
	fisica4 = models.IntegerField(default=0, blank=True, null=True)
	fisica5 = models.IntegerField(default=0, blank=True, null=True)
	fisicapromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	artistica1 = models.IntegerField(default=0, blank=True, null=True)
	artistica2 = models.IntegerField(default=0, blank=True, null=True)
	artistica3 = models.IntegerField(default=0, blank=True, null=True)
	artistica4 = models.IntegerField(default=0, blank=True, null=True)
	artistica5 = models.IntegerField(default=0, blank=True, null=True)
	artisticapromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	aviso1 = models.BooleanField(default=False)
	aviso2 = models.BooleanField(default=False)
	aviso3 = models.BooleanField(default=False)

	def __unicode__(self):
		return self.codigoboleta

	class Meta:
		permissions = (
            ("ver_boleta4", "Permiso para visualizar las boletas de cuarto"),
        )

class Boleta5(models.Model):
	codigoboleta = models.CharField(max_length=50, blank=True)
	idprofesor=  models.ForeignKey(Personal)
	idgrupo =  models.ForeignKey(Grupo)
	idalumno = models.ForeignKey(Alumno)
	idescuela = models.ForeignKey(Escuela)
	cicloescolar = models.CharField(max_length=50, blank=True, null=True)
	fechadevalidacion = models.DateField(default=datetime.now, blank=True, null=True, )
	lugardevalidacion =models.CharField(default="-", max_length=50, blank=True, null=True)
	promovido = models.BooleanField(default=False)
	promedio = models.DecimalField(max_digits = 3, decimal_places = 1,default=0.0, blank=True, null=True)
	inasistencias1= models.IntegerField(default=0, blank=True, null=True)
	inasistencias2= models.IntegerField(default=0, blank=True, null=True)
	inasistencias3= models.IntegerField(default=0, blank=True, null=True)
	inasistencias4= models.IntegerField(default=0, blank=True, null=True)
	inasistencias5= models.IntegerField(default=0, blank=True, null=True)
	inasistenciastotal= models.IntegerField(default=0, blank=True, null=True)
	espanol1 = models.IntegerField(default=0, blank=True, null=True)
	espanol2 = models.IntegerField(default=0, blank=True, null=True)
	espanol3 = models.IntegerField(default=0, blank=True, null=True)
	espanol4 = models.IntegerField(default=0, blank=True, null=True)
	espanol5 = models.IntegerField(default=0, blank=True, null=True)
	espanolpromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	matematicas1 = models.IntegerField(default=0, blank=True, null=True)
	matematicas2 = models.IntegerField(default=0, blank=True, null=True)
	matematicas3 = models.IntegerField(default=0, blank=True, null=True)
	matematicas4 = models.IntegerField(default=0, blank=True, null=True)
	matematicas5 = models.IntegerField(default=0, blank=True, null=True)
	matematicaspromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	ciencias1 = models.IntegerField(default=0, blank=True, null=True)
	ciencias2 = models.IntegerField(default=0, blank=True, null=True)
	ciencias3 = models.IntegerField(default=0, blank=True, null=True)
	ciencias4 = models.IntegerField(default=0, blank=True, null=True)
	ciencias5 = models.IntegerField(default=0, blank=True, null=True)
	cienciaspromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	geografia1 = models.IntegerField(default=0, blank=True, null=True)
	geografia2 = models.IntegerField(default=0, blank=True, null=True)
	geografia3 = models.IntegerField(default=0, blank=True, null=True)
	geografia4 = models.IntegerField(default=0, blank=True, null=True)
	geografia5 = models.IntegerField(default=0, blank=True, null=True)
	geografiapromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	historia1 = models.IntegerField(default=0, blank=True, null=True)
	historia2 = models.IntegerField(default=0, blank=True, null=True)
	historia3 = models.IntegerField(default=0, blank=True, null=True)
	historia4 = models.IntegerField(default=0, blank=True, null=True)
	historia5 = models.IntegerField(default=0, blank=True, null=True)
	historiapromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	formacion1 = models.IntegerField(default=0, blank=True, null=True)
	formacion2 = models.IntegerField(default=0, blank=True, null=True)
	formacion3 = models.IntegerField(default=0, blank=True, null=True)
	formacion4 = models.IntegerField(default=0, blank=True, null=True)
	formacion5 = models.IntegerField(default=0, blank=True, null=True)
	formacionpromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	fisica1 = models.IntegerField(default=0, blank=True, null=True)
	fisica2 = models.IntegerField(default=0, blank=True, null=True)
	fisica3 = models.IntegerField(default=0, blank=True, null=True)
	fisica4 = models.IntegerField(default=0, blank=True, null=True)
	fisica5 = models.IntegerField(default=0, blank=True, null=True)
	fisicapromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	artistica1 = models.IntegerField(default=0, blank=True, null=True)
	artistica2 = models.IntegerField(default=0, blank=True, null=True)
	artistica3 = models.IntegerField(default=0, blank=True, null=True)
	artistica4 = models.IntegerField(default=0, blank=True, null=True)
	artistica5 = models.IntegerField(default=0, blank=True, null=True)
	artisticapromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	aviso1 = models.BooleanField(default=False)
	aviso2 = models.BooleanField(default=False)
	aviso3 = models.BooleanField(default=False)

	def __unicode__(self):
		return self.codigoboleta

	class Meta:
		permissions = (
            ("ver_boleta5", "Permiso para visualizar las boletas de quinto"),
        )

class Boleta6(models.Model):
	codigoboleta = models.CharField(max_length=50, blank=True)
	idprofesor=  models.ForeignKey(Personal)
	idgrupo =  models.ForeignKey(Grupo)
	idalumno = models.ForeignKey(Alumno)
	idescuela = models.ForeignKey(Escuela)
	cicloescolar = models.CharField(max_length=50, blank=True, null=True)
	fechadevalidacion = models.DateField(default=datetime.now, blank=True, null=True, )
	lugardevalidacion =models.CharField(default="-", max_length=50, blank=True, null=True)
	promovido = models.BooleanField(default=False)
	promedio = models.DecimalField(max_digits = 3, decimal_places = 1,default=0.0, blank=True, null=True)
	inasistencias1= models.IntegerField(default=0, blank=True, null=True)
	inasistencias2= models.IntegerField(default=0, blank=True, null=True)
	inasistencias3= models.IntegerField(default=0, blank=True, null=True)
	inasistencias4= models.IntegerField(default=0, blank=True, null=True)
	inasistencias5= models.IntegerField(default=0, blank=True, null=True)
	inasistenciastotal= models.IntegerField(default=0, blank=True, null=True)
	espanol1 = models.IntegerField(default=0, blank=True, null=True)
	espanol2 = models.IntegerField(default=0, blank=True, null=True)
	espanol3 = models.IntegerField(default=0, blank=True, null=True)
	espanol4 = models.IntegerField(default=0, blank=True, null=True)
	espanol5 = models.IntegerField(default=0, blank=True, null=True)
	espanolpromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	matematicas1 = models.IntegerField(default=0, blank=True, null=True)
	matematicas2 = models.IntegerField(default=0, blank=True, null=True)
	matematicas3 = models.IntegerField(default=0, blank=True, null=True)
	matematicas4 = models.IntegerField(default=0, blank=True, null=True)
	matematicas5 = models.IntegerField(default=0, blank=True, null=True)
	matematicaspromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	ciencias1 = models.IntegerField(default=0, blank=True, null=True)
	ciencias2 = models.IntegerField(default=0, blank=True, null=True)
	ciencias3 = models.IntegerField(default=0, blank=True, null=True)
	ciencias4 = models.IntegerField(default=0, blank=True, null=True)
	ciencias5 = models.IntegerField(default=0, blank=True, null=True)
	cienciaspromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	geografia1 = models.IntegerField(default=0, blank=True, null=True)
	geografia2 = models.IntegerField(default=0, blank=True, null=True)
	geografia3 = models.IntegerField(default=0, blank=True, null=True)
	geografia4 = models.IntegerField(default=0, blank=True, null=True)
	geografia5 = models.IntegerField(default=0, blank=True, null=True)
	geografiapromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	historia1 = models.IntegerField(default=0, blank=True, null=True)
	historia2 = models.IntegerField(default=0, blank=True, null=True)
	historia3 = models.IntegerField(default=0, blank=True, null=True)
	historia4 = models.IntegerField(default=0, blank=True, null=True)
	historia5 = models.IntegerField(default=0, blank=True, null=True)
	historiapromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	formacion1 = models.IntegerField(default=0, blank=True, null=True)
	formacion2 = models.IntegerField(default=0, blank=True, null=True)
	formacion3 = models.IntegerField(default=0, blank=True, null=True)
	formacion4 = models.IntegerField(default=0, blank=True, null=True)
	formacion5 = models.IntegerField(default=0, blank=True, null=True)
	formacionpromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	fisica1 = models.IntegerField(default=0, blank=True, null=True)
	fisica2 = models.IntegerField(default=0, blank=True, null=True)
	fisica3 = models.IntegerField(default=0, blank=True, null=True)
	fisica4 = models.IntegerField(default=0, blank=True, null=True)
	fisica5 = models.IntegerField(default=0, blank=True, null=True)
	fisicapromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	artistica1 = models.IntegerField(default=0, blank=True, null=True)
	artistica2 = models.IntegerField(default=0, blank=True, null=True)
	artistica3 = models.IntegerField(default=0, blank=True, null=True)
	artistica4 = models.IntegerField(default=0, blank=True, null=True)
	artistica5 = models.IntegerField(default=0, blank=True, null=True)
	artisticapromedio = models.DecimalField(max_digits=3, decimal_places=1,default=0.0, blank=True, null=True)
	aviso1 = models.BooleanField(default=False)
	aviso2 = models.BooleanField(default=False)
	aviso3 = models.BooleanField(default=False)

	def __unicode__(self):
		return self.codigoboleta

	class Meta:
		permissions = (
            ("ver_boleta6", "Permiso para visualizar las boletas de sexto"),
        )

class Tarea(models.Model):
	idgrupo=  models.ForeignKey(Grupo)
	autor = models.CharField(max_length=50, blank=True)	
	titulo = models.CharField(max_length=50, blank=True)	
	fechapublica = models.DateField(blank=True, null=True, auto_now=True )
	fechatarea= models.DateField(blank=True, null=True)
	tarea = models.TextField(max_length=200, blank=True)	
	
	def __unicode__(self):
		return unicode(self.idgrupo)+ ' ' +unicode(self.fechatarea) 
	class Meta:
		permissions = (
            ("ver_tarea", "Permiso ver_tarea"),
        )

class Consejo(models.Model):
	director=  models.ForeignKey(Personal)
	#profesor=  models.ForeignKey(Personal)
	