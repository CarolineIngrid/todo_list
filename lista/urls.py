from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista'),
    path('new/', views.TarefasNew.as_view(), name='lista_new'),
]
