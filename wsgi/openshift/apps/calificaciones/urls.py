from django.conf.urls import patterns, include, url
from .views import calificaciones,vercalificaciones,registrarcalificaciones,registraralumno,alumno,personal,eliminartarea,registrarpersonal,registrartutor,tutor,tareas,creartareas,grupo,registrargrupo

urlpatterns = patterns('',
	url(r'^calificaciones/(?P<pk>[\w-]+)$', calificaciones.as_view(), name='calificaciones'),
	url(r'^vercalificaciones/$', vercalificaciones.as_view(), name='vercalificaciones'),
	  #vista a donde se envia una vez que se completa el formulario

	url(r'^registrarpersonal/$', registrarpersonal.as_view(), name='registrarpersonal'), 
	url(r'^personal/$', personal.as_view(), name='personal'),

	url(r'^registraralumno/$', registraralumno.as_view(), name='registraralumno'), 
	url(r'^alumno/$', alumno.as_view(), name='alumno'),

	url(r'^registrartutor/$', registrartutor.as_view(), name='registrartutor'), 
	url(r'^tutor/$', tutor.as_view(), name='tutor'),

	url(r'^registrargrupo/$', registrargrupo.as_view(), name='registrargrupo'), 
	url(r'^grupo/$', grupo.as_view(), name='grupo'),


	url(r'^registrarcalificaciones/', registrarcalificaciones.as_view(), name='registrarcalificaciones'),

	url(r'^tareas/$', tareas.as_view(), name='tareas'),
	url(r'^creartareas/$', creartareas.as_view(), name='creartareas'),
	url(r'^eliminartarea/(?P<pk>[\w-]+)/delete/$', eliminartarea.as_view(), name='eliminartarea'),
   
)
