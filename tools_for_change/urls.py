from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tfc', views.index, name='index'),
    path('about', views.about, name='about'),
    path('aframe', views.aframe, name='aframe'),
]
