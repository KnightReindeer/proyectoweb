from django.conf.urls import patterns, include, url
from .views import calificaciones,registrarcalificaciones,personal,registrarpersonal,tareas,creartareas


urlpatterns = patterns('',
	url(r'^calificaciones/$', calificaciones.as_view(), name='calificaciones'),

	  #vista a donde se envia una vez que se completa el formulario

	url(r'^registrarpersonal/$', registrarpersonal.as_view(), name='registrarpersonal'), 
	url(r'^personal/$', personal.as_view(), name='personal'),

	url(r'^registrarcalificaciones/$', registrarcalificaciones.as_view(), name='registrarcalificaciones'),

	url(r'^tareas/$', tareas.as_view(), name='tareas'),
	url(r'^creartareas/$', creartareas.as_view(), name='creartareas'),
   
)
