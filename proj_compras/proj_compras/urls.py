"""proj_compras URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),

    #login-users
    url(r'^',
        include('usuarios.urls',  namespace='usuarios')
        ),

    # Login/Logout URLs
    #(r'^login/$',
    #    'django.contrib.auth.views.login', {'template_name': 'login.html'}
    #),

    #(r'^logout/$',
    #    'django.contrib.auth.views.logout', {'next_page': '/login/'}
    #),

    url(r'^proveedores/',
        include('proveedores.urls', namespace='proveedores')
        ),

    url(r'^contactos/',
        include('contactos.urls', namespace='contactos')
        ),
)
