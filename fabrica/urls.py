# En tu archivo urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('tareas/', views.lista_tareas, name='lista_tareas'),
    path('tareas/crear/', views.crear_tarea, name='crear_tarea'),
    path('tareas/<int:id>/', views.detalle_tarea, name='detalle_tarea'),
    path('tareas/<int:id>/modificar/', views.modificar_tarea, name='modificar_tarea'),
    path('tareas/<int:id>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
    path('crear_fabrica/', views.crear_fabrica, name='crear_fabrica'),
    path('crear_costurera/', views.crear_costurera, name='crear_costurera'),
    path('costureras/<str:identificacion>/eliminar/', views.eliminar_costurera, name='eliminar_costurera')
]
