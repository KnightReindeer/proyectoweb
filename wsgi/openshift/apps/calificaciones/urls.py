from django.conf.urls import patterns, include, url
from .views import calificaciones,vercalificaciones,calificaciones6,vercalificaciones5,vercalificaciones6,calificaciones5,calificaciones2,calificaciones4,vercalificaciones4,calificaciones3,vercalificaciones2,vercalificaciones3,registrarcalificaciones,registraralumno,alumno,personal,eliminartarea,registrarpersonal,registrartutor,tutor,tareas,creartareas,grupo,registrargrupo

urlpatterns = patterns('',
	url(r'^calificaciones/(?P<pk>[\w-]+)$', calificaciones.as_view(), name='calificaciones'),
	url(r'^calificaciones2/(?P<pk>[\w-]+)$', calificaciones2.as_view(), name='calificaciones2'),
	url(r'^calificaciones3/(?P<pk>[\w-]+)$', calificaciones3.as_view(), name='calificaciones3'),
	url(r'^calificaciones4/(?P<pk>[\w-]+)$', calificaciones4.as_view(), name='calificaciones4'),
	url(r'^calificaciones5/(?P<pk>[\w-]+)$', calificaciones5.as_view(), name='calificaciones5'),
	url(r'^calificaciones6/(?P<pk>[\w-]+)$', calificaciones6.as_view(), name='calificaciones6'),

	url(r'^vercalificaciones1([\w-]*)/$', vercalificaciones.as_view(), name='vercalificaciones'),
	url(r'^vercalificaciones2([\w-]*)/$', vercalificaciones2.as_view(), name='vercalificaciones2'),
	url(r'^vercalificaciones3([\w-]*)/$', vercalificaciones3.as_view(), name='vercalificaciones3'),
	url(r'^vercalificaciones4([\w-]*)/$', vercalificaciones4.as_view(), name='vercalificaciones4'),
	url(r'^vercalificaciones5([\w-]*)/$', vercalificaciones5.as_view(), name='vercalificaciones5'),
	url(r'^vercalificaciones6([\w-]*)/$', vercalificaciones6.as_view(), name='vercalificaciones6'),

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
