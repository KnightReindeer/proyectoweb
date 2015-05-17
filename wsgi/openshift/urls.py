from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyectoweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
    url(r'^', include('apps.inicio.urls')),

    url(r'^', include('apps.calificaciones.urls')),

    url(r'^', include('apps.pizarron.urls')),

)
