from django.contrib import admin
from django.urls import path
from . import views
from . import apiview


urlpatterns = [
    path('index',views.index, name='index'),
    path('profile',views.Profile, name='profile'),
    path('vote',views.vote,name='vote'),
    path('results/<poll_id>/',views.results,name='results'),
    path('',views.login,name="login"),
    path('reg',views.reg,name="reg"),
    path('create',views.create,name="create"),
    path('vote/<poll_id>/',views.vote,name="vote"),
    path('delete/<int:id>/',views.Delete,name="delete"),
    path('logout/',views.logout,name='logout'),
    path('questions/', apiview.questions_view, name='questions_view'),

    

    path('plogin',views.plogin,name="plogin"),
    path('preg',views.preg,name="preg"),
    path('pindex',views.pindex,name='pindex'),
    path('plogout/',views.plogout,name='plogout'),
      
]
