from django.urls import path 
from .views import ( index,ListaTareasView, DetalleTareaView, 
AgregarTareaView, EliminarTareaView, RegistroView, CustomLoginView, logout_view ) 

urlpatterns = [ 
    path('', index, name='index'), 
    path('lista/', ListaTareasView.as_view(), name='lista_tareas'), 
    path('tarea/<int:pk>/', DetalleTareaView.as_view(), name='detalle_tarea'), 
    path('agregar/', AgregarTareaView.as_view(), name='agregar_tarea'), 
    path('eliminar/<int:pk>/', EliminarTareaView.as_view(), name='eliminar_tarea'), 
    path('login/', CustomLoginView.as_view(), name='login'), 
    path('registro/', RegistroView.as_view(), name='registro'), path('logout/', logout_view, name='logout'), 
]
