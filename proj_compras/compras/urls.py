from django.conf.urls import patterns, url

from . import views

urlpatterns = [

    url(regex=r'^solicitudes/$',
        view=views.SolicitudDeCompraList.as_view(),
        name='lista_solicitudes'
        ),

    url(regex=r'^solicitudes/nueva$',
        view=views.solicitud_de_compra_cru,
        name='nueva_solicitud'
        ),

    url(regex=r'^solicitudes/(?P<pk>[\w-]+)/editar/$',
        view=views.solicitud_de_compra_cru,
        name='editar_solicitud'
        ),

    url(regex=r'^solicitudes/(?P<pk>[\w-]+)/$',
        view=views.detalle_solicitud_de_compra,
        name='detalle_solicitud'
        ),

    url(regex=r'^solicitudes/(?P<pk>[\w-]+)/borrar/$',
        view=views.BorrarSolicitudDeCompra.as_view(),
        name='borrar_solicitud'
        ),

]
