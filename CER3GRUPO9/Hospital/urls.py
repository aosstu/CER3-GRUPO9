from django.contrib import admin
from django.urls import path
from Hospital import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Inicio/', views.vistaPadres, name="VerBebes"),
    path('Avances/',views.Avances, name="verAvances"),
    path('nuevoAvance/',views.nuevoAvance, name='añadirAvance'),
    path('',views.login),
    path('modificarAvance/<id>/',views.modificarAvance, name='modificarAvance'),
    path('eliminarAvance/<id>/',views.eliminarAvance,name='eliminarAvance'),
]
