from django.db import models

# Create your models here.

class Profesor(models.Model):
	nombre = models.CharField(max_length=50, blank=True)
	clavepresupuestal = models.CharField(max_length=45, blank=True)
	fechanacimiento = models.DateField(blank=True, null=True)
	
	def __unicode__(self):
		return self.nombre

class Grupo(models.Model):
	grupo = models.CharField(max_length=10, blank=True) #se ingresa  2 A , 3C, ETC
	idprofesor = models.ForeignKey(Profesor)
	def __unicode__(self):
		return self.grupo

class Alumno(models.Model):
	nombrea = models.CharField(max_length=50, blank=True)
	curp = models.CharField(max_length=45, blank=True)
	fechanacimiento = models.DateField(blank=True, null=True)
	idgrupo = models.ForeignKey(Grupo)
	def __unicode__(self):
		return self.nombrea



class Boleta(models.Model):
	codigoboleta= models.CharField(max_length=50, blank=True)
	idgrupo=  models.ForeignKey(Grupo)
	idalumno = models.ForeignKey(Alumno)
	espanol = models.IntegerField()
	matematicas = models.IntegerField()
	exploracion = models.IntegerField()
	formacion = models.IntegerField()
	fisica = models.IntegerField()
	artistica = models.IntegerField()

	
	def __unicode__(self):
		return unicode(self.idgrupo) + ' ' + str(self.idalumno)

class Tarea(models.Model):
	idgrupo=  models.ForeignKey(Grupo)
	tarea = models.TextField(max_length=100, blank=True)	
	#def __unicode__(self):
	#	return self.idgrupo