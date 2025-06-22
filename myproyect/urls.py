from django.urls import path
from . import views

urlpatterns = [
    # HOME
    path('', views.home, name='home'),

    # CARTERAS
    path('carteras/', views.lista_carteras, name='lista_carteras'),
    path('carteras/<int:pk>/', views.detalle_cartera, name='detalle_cartera'),
    path('carteras/crear/', views.crear_cartera, name='crear_cartera'),
    path('carteras/eliminar/<int:pk>/', views.eliminar_cartera, name='eliminar_cartera'),

    # BILLETERAS
    path('billeteras/', views.lista_billeteras, name='lista_billeteras'),
    path('billeteras/<int:pk>/', views.detalle_billetera, name='detalle_billetera'),
    path('billeteras/crear/', views.crear_billetera, name='crear_billetera'),
    path('billeteras/eliminar/<int:pk>/', views.eliminar_billetera, name='eliminar_billetera'),

    # CINTOS
    path('cintos/', views.lista_cintos, name='lista_cintos'),
    path('cintos/<int:pk>/', views.detalle_cinto, name='detalle_cinto'),
    path('cintos/crear/', views.crear_cinto, name='crear_cinto'),
    path('cintos/eliminar/<int:pk>/', views.eliminar_cinto, name='eliminar_cinto'),

    # ABOUT
    path('about/', views.about, name='about'),

    # REGISTRO
    path('registro/', views.registro, name='registro'),

]
