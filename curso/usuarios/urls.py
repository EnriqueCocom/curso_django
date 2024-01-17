from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("borrar/", views.borrar, name="borrar"),
    path("suma/", views.calcula_suma, name="suma"),
]

