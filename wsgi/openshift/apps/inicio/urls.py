from django.conf.urls import patterns, include, url
from .views import index, reglamento, estructura
from django.contrib.auth import logout


urlpatterns = patterns('',
       url(r'^$', index.as_view(),name = 'index'),
       url(r'^reglamento/$',reglamento.as_view()),
       #url(r'^estructura organica/$',estructura.as_view()),

       url(r'^login/$', 'django.contrib.auth.views.login',{'template_name':'inicio/login.html'},name = 'login'),
       url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login',name = 'logout'),
)
