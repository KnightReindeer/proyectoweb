from django.conf.urls import patterns, include, url
from .views import calificaciones,vercalificaciones,actualizaralumno,calificaciones6,vercalificaciones5
from .views import vercalificaciones6,calificaciones5,calificaciones2,calificaciones4,vercalificaciones4
from .views import calificaciones3,vercalificaciones2,vercalificaciones3,registrarcalificaciones
from .views import registraralumno,alumno,personal,eliminartarea,registrarpersonal,registrartutor,tutor
from .views import tareas,creartareas,grupo,registrargrupo,editargrupo, eliminargrupo,actualizartutor
from .views import eliminartutor,eliminaralumno,actualizarpersonal, eliminarpersonal, registrarcalificaciones2,registrarcalificaciones3, registrarcalificaciones4, registrarcalificaciones5, registrarcalificaciones6

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
	url(r'^actualizaralumno/(?P<pk>[\w-]+)$', actualizaralumno.as_view(), name='actualizaralumno'),
	url(r'^actualizartutor/(?P<pk>[\w-]+)$', actualizartutor.as_view(), name='actualizartutor'),

	url(r'^actualizarpersonal/(?P<pk>[\w-]+)$', actualizarpersonal.as_view(), name='actualizarpersonal'),

	url(r'^registrartutor/$', registrartutor.as_view(), name='registrartutor'), 
	url(r'^tutor/$', tutor.as_view(), name='tutor'),

	url(r'^registrargrupo/$', registrargrupo.as_view(), name='registrargrupo'), 
	url(r'^grupo/$', grupo.as_view(), name='grupo'),


	url(r'^registrarcalificaciones/', registrarcalificaciones.as_view(), name='registrarcalificaciones'),
	url(r'^registrarcalificaciones2/', registrarcalificaciones2.as_view(), name='registrarcalificaciones2'),
	url(r'^registrarcalificaciones3/', registrarcalificaciones3.as_view(), name='registrarcalificaciones3'),
	url(r'^registrarcalificaciones4/', registrarcalificaciones4.as_view(), name='registrarcalificaciones4'),


	url(r'^registrarcalificaciones5/', registrarcalificaciones5.as_view(), name='registrarcalificaciones5'),

	url(r'^registrarcalificaciones6/', registrarcalificaciones6.as_view(), name='registrarcalificaciones6'),

	
	url(r'^editargrupo/(?P<pk>[\w-]+)$', editargrupo.as_view(), name='editargrupo'),

	url(r'^tareas/$', tareas.as_view(), name='tareas'),
	url(r'^creartareas/$', creartareas.as_view(), name='creartareas'),

	url(r'^eliminartarea/(?P<pk>[\w-]+)/delete/$', eliminartarea.as_view(), name='eliminartarea'),
	url(r'^eliminargrupo/(?P<pk>[\w-]+)/delete/$', eliminargrupo.as_view(), name='eliminargrupo'),
	url(r'^eliminartutor/(?P<pk>[\w-]+)/delete/$', eliminartutor.as_view(), name='eliminartutor'),
	url(r'^eliminaralumno/(?P<username>[\w-]+)/delete/$', eliminaralumno.as_view(), name='eliminaralumno'),
	url(r'^eliminarpersonal/(?P<username>[\w-]+)/delete/$', eliminarpersonal.as_view(), name='eliminarpersonal'),   
)
