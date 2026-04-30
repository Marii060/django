
#URL configuration for crud project.

from django.contrib import admin
from django.urls import path
from tareas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('tareas/', views.lista_tareas, name="lista_tareas"),
    path('tarea/<int:pk>/', views.detalle_tarea, name="detalle_tarea"),
    path('tarea/nueva/', views.crear_tarea, name="crear_tarea"),
    # esos <> se colocan porque van a estar cambiando constantemente
    path('tarea/<int:pk>/editar/', views.editar_tarea, name="editar_tarea"),
    path('tarea/<int:pk>/eliminar/', views.eliminar_tarea, name="eliminar_tarea"),
]

