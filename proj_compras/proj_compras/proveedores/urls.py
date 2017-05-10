from django.conf.urls import url

from .views import ProveedoresList

urlpatterns = [

    url(regex=r'^$',
        view=ProveedoresList.as_view(),
        name='list'
        )

]
