#Configurando redireccionamiento 
from django.urls import path
from . import views 
urlpatterns = [
    path('',views.home, name='home'),
    path('listadoGeneros/',views.listadoGeneros, name='listadoGeneros'),
    path('eliminarGenero/<id>',views.eliminarGenero, name='eliminarGenero'),
    path('nuevoGenero/',views.nuevoGenero, name='nuevoGenero'),
    path('guardarGenero/',views.guardarGenero, name='guardarGenero'),
    path('editarGenero/<id>',views.editarGenero, name='editarGenero'),
    path('procesarActualizacionGenero/',views.procesarActualizacionGenero, name='procesarActualizacionGenero'),
    path('listadoDirectores/',views.listadoDirectores, name='listadoDirectores'),
    
    path('listadoDirectores/', views.listadoDirectores, name='listadoDirectores'),
    path('eliminarDirector/<id>', views.eliminarDirector, name='eliminarDirector'),
    path('nuevoDirector/', views.nuevoDirector, name='nuevoDirector'),
    path('guardarDirector/', views.guardarDirector, name='guardarDirector'),
    path('editarDirector/<id>', views.editarDirector, name='editarDirector'),
    path('procesarActualizacionDirector/', views.procesarActualizacionDirector, name='procesarActualizacionDirector'),

    path('listadoPais/',views.listadoPais, name='listadoPais'),
    path('listadoPeliculas/',views.listadoPeliculas, name='listadoPeliculas'),

    path('gestionCines/',views.gestionCines, name='gestionCines'),
    path('guardarCine/',views.guardarCine, name='guardarCine'),
    path('listadoCines/',views.listadoCines, name='listadoCines'),

    #Directores Y Peliculas
    path('gestionDirectores/', views.gestionDirectores, name='gestionDirectores'),
    path('gestionPeliculas/', views.gestionPeliculas, name='gestionPeliculas'),
    path('insertar_director/', views.insertar_director, name='insertar_director'),
    path('insertar_pelicula/', views.insertar_pelicula, name='insertar_pelicula'),
    path('consultar_directores/', views.consultar_directores, name='consultar_directores'),
    path('consultar_peliculas/', views.consultar_peliculas, name='consultar_peliculas'),
]

