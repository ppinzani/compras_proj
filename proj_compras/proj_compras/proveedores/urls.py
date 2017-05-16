from django.conf.urls import patterns, url

from . import views

urlpatterns = [

    url(regex=r'^$',
        view=views.ProveedoresList.as_view(),
        name='lista'
        ),

    url(regex=r'^nuevo/$',
        view=views.proveedor_cru,
        name='nuevo'
        ),

    url(regex=r'^(?P<uuid>[\w-]+)/editar/$',
        view=views.proveedor_cru,
        name='editar'
        ),


    url(regex=r'^(?P<uuid>[\w-]+)/$',
        view=views.detalle_proveedor,
        name='detalle'
        ),

]
