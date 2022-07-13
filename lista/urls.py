from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista'),
    path('new', views.lista_new, name='lista_new'),
]
