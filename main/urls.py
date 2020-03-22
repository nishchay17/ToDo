from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.show, name='show' ),
    path('complete/<todoId>', views.todoComplete, name= 'complete'),
    path('delete', views.delete, name= 'delete'),
    path('deleteAll', views.deleteAll, name= 'deleteAll')
]