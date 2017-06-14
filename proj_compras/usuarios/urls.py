from django.conf.urls import url

from . import views

urlpatterns = [

    url(regex=r'^$',
        view=views.user_login,
        name='login'
        ),

    url(regex=r'^logout/$',
        view=views.user_logout,
        name='logout'
        ),

#principal
    #url(r'^home', Home.as_view(), name='home'),
]
