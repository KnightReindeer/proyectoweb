from django.db import models
from datetime import datetime
# Create your models here.

class Avisos(models.Model):
	titulo = models.CharField(max_length=20, blank=True)
	fechaa = models.DateField(blank=True, null=True) 
	texto = models.TextField(max_length=200, blank=True) #se ingresa el texto del aviso
	#imagen = models.ImageField(upload_to='avisosimg', blank=True)
	def __unicode__(self):
		return unicode (self.fechaa)

	class Meta:
		permissions = (
            ("ver_aviso", "Permiso ver_aviso"),
        )
