from django.conf.urls import patterns, url

from . import views

urlpatterns = [

    url(regex=r'^$',
        view=views.MercaderiasList.as_view(),
        name='lista'
        ),

    url(regex=r'^nuevo/$',
        view=views.CrearMercaderia.as_view(),
        name='nuevo'
        ),

    url(regex=r'^(?P<pk>[\w-]+)/editar/$',
        view=views.ActualizarMercaderia.as_view(),
        name='editar'
        ),

    url(regex=r'^(?P<pk>[\w-]+)/borrar/$',
        view=views.EliminarMercaderia.as_view(),
        name='borrar'
        ),

    url(regex=r'^categorias/$',
        view=views.CategoriasList.as_view(),
        name='lista_categorias'
        ),

    url(regex=r'^categorias/nuevo/$',
        view=views.CrearCategoria.as_view(),
        name='nueva_categoria'
        ),

    url(regex=r'^categorias/(?P<pk>[\w-]+)/editar/$',
        view=views.ActualizarCategoria.as_view(),
        name='editar_categoria'
        ),

    url(regex=r'^categorias/(?P<pk>[\w-]+)/borrar/$',
        view=views.EliminarCategoria.as_view(),
        name='borrar_categoria'
        ),

]
