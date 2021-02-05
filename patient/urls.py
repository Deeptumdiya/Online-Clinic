from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('patindex',views.patindex , name='patindex'),
    path('pregs', views.pregs,name='pregs'),
    path('psignup', views.psignup,name='psignup'),
    path('plogin', views.plogin,name='plogin'),
    path('searchdoc', views.searchdoc,name='searchdoc'),
    path('appointment', views.bookappoint,name='bookappoint'),
    path('showpres', views.showpres,name='showpres'),
] 