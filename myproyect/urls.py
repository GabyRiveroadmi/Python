from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar_cartera/', views.agregar_cartera, name='agregar_cartera'),
    path('agregar_billetera/', views.agregar_billetera, name='agregar_billetera'),
    path('agregar_cinto/', views.agregar_cinto, name='agregar_cinto'),
    path('buscar/', views.buscar_producto, name='buscar'),
    path('resultados/', views.resultados_busqueda, name='resultados'),
]
