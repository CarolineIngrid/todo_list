from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista'),
    path('new/', views.TarefasNew.as_view(), name='lista_new'),
    path('delete/<tarefa_id>', views.delete, name='lista_delete'),
    path('riscado/<tarefa_id>', views.riscado, name='tarefa_feita'),
    path('não_riscado/<tarefa_id>', views.nao_riscado, name='nao_feita'),
]
