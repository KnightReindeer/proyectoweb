from django.conf.urls import patterns, include, url
from .views import avisos, crearavisos,eliminaraviso


urlpatterns = patterns('',
	url(r'^avisos/$', avisos.as_view(), name='avisos'),
	url(r'^crearavisos/$', crearavisos.as_view(), name='crearavisos'),
	url(r'^eliminaraviso/(?P<pk>[\w-]+)/delete/$', eliminaraviso.as_view(), name='eliminaraviso'),
)
