from django.conf.urls import patterns, include, url
from .views import avisos, crearavisos


urlpatterns = patterns('',
	url(r'^avisos/$', avisos.as_view(), name='avisos'),
	url(r'^crearavisos/$', crearavisos.as_view(), name='crearavisos'),
)
