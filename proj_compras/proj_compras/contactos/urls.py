from django.conf.urls import patterns, url

from . import views

urlpatterns = [

    url(regex=r'^nuevo/$',
        view=views.contacto_cru,
        name='nuevo'
        ),

    url(regex=r'^(?P<uuid>[\w-]+)/editar/$',
        view=views.contacto_cru,
        name='editar'
        ),

    url(regex=r'^(?P<pk>[\w-]+)/borrar/$',
        view=views.BorrarContacto.as_view(),
        name='borrar'
        ),

    url(regex=r'^(?P<uuid>[\w-]+)/$',
        view=views.detalle_contacto,
        name='detalle'
        ),

]
