"""
Definition of urls for reinet.
"""

from datetime import datetime
from django.conf.urls import patterns, url, include
from app.forms import BootstrapAuthenticationForm
from usuarios.views import *

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

#Jorge
urlpatterns = patterns('',
    # Examples:
   # url(r'^$', 'app.views.home', name='home'),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    url(r'^incubaciones$','concursoIncubacion.views.homeIncubaciones',name='incubaciones'),
    url(r'^demanda$','ofertaDemanda.views.DemandaInicio',name='demanda'),
    url(r'^oferta$','ofertaDemanda.views.OfertaInicio',name='oferta'),
    url(r'^',include('usuarios.urls')),
    url(r'^',include('concursoIncubacion.urls')),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
