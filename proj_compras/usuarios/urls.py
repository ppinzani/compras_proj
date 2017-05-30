from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex=r'^$',
        view=views.userlogin,
        name='login'
        ),


    #url(r'^salir/$', 'apps.users.views.LogOut', name = 'logout'),
#principal
    #url(r'^home', Home.as_view(), name='home'),
]
