from django.conf.urls import patterns, include, url
from .views import calificaciones,registrarcalificaciones,registraralumno,alumno,personal,registrarpersonal,registrartutor,tutor,tareas,creartareas,grupo,registrargrupo

urlpatterns = patterns('',
	url(r'^calificaciones/$', calificaciones.as_view(), name='calificaciones'),

	  #vista a donde se envia una vez que se completa el formulario

	url(r'^registrarpersonal/$', registrarpersonal.as_view(), name='registrarpersonal'), 
	url(r'^personal/$', personal.as_view(), name='personal'),

	url(r'^registraralumno/$', registraralumno.as_view(), name='registraralumno'), 
	url(r'^alumno/$', alumno.as_view(), name='alumno'),

	url(r'^registrartutor/$', registrartutor.as_view(), name='registrartutor'), 
	url(r'^tutor/$', tutor.as_view(), name='tutor'),

	url(r'^registrargrupo/$', registrargrupo.as_view(), name='registrargrupo'), 
	url(r'^grupo/$', grupo.as_view(), name='grupo'),

	url(r'^registrarcalificaciones/$', registrarcalificaciones.as_view(), name='registrarcalificaciones'),

	url(r'^tareas/$', tareas.as_view(), name='tareas'),
	url(r'^creartareas/$', creartareas.as_view(), name='creartareas'),
   
)
