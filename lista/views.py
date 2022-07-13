from django.shortcuts import render
from .models import Tarefa

from urllib import request

# Create your views here.
def lista_tarefas(request):
    lista_tarefas = Tarefa.objects.all()
    status = request.GET.get('status')
    print(status)
    return render(request, 'lista/index.html', {'lista_tarefas':lista_tarefas})
