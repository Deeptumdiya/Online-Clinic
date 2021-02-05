from django.contrib import admin
from django.urls import path
from . import views
from django.views import View
from doctor.views import Login

urlpatterns = [
    path('', views.index,name='index'),
    path('doc/', views.docindex, name='docindex'),
    path('doc/dlogin',Login.as_view()),
    path('doc/getdocappoint', views.getdocappoint,name='getdocappoint'),
    path('doc/priscribed', views.priscribed,name='priscribed'),
    path('doc/logout', views.logout,name='logout'),
]
