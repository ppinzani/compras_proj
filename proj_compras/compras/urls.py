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

    url(regex=r'^solicitudes/(?P<pk>[\w-]+)/aprobar/$',
        view=views.AprobarSolicitudDeCompra.as_view(),
        name='aprobar_solicitud'
        ),

    url(regex=r'^cotizaciones/$',
        view=views.CotizacionesList.as_view(),
        name='lista_cotizaciones'
        ),

    url(regex=r'^cotizaciones/nueva/$',
        view=views.cotizacion_cru,
        name='nueva_cotizacion'
        ),

    url(regex=r'^cotizaciones/(?P<pk>[\w-]+)/editar/$',
        view=views.cotizacion_cru,
        name='editar_cotizacion'
        ),

    url(regex=r'^cotizaciones/(?P<pk>[\w-]+)/$',
        view=views.detalle_cotizacion,
        name='detalle_cotizacion'
        ),

    url(regex=r'^cotizaciones/(?P<pk>[\w-]+)/borrar/$',
        view=views.BorrarCotizacion.as_view(),
        name='borrar_cotizacion'
        ),

    url(regex=r'^cotizaciones/(?P<pk>[\w-]+)/aprobar/$',
        view=views.AprobarCotizacion.as_view(),
        name='aprobar_cotizacion'
        ),

    url(regex=r'^cotizaciones/(?P<pk>[\w-]+)/rechazar/$',
        view=views.RechazarCotizacion.as_view(),
        name='rechazar_cotizacion'
        ),
]
