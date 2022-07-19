from django.shortcuts import render, reverse, redirect
from django.views.generic import CreateView

from .forms import ListaForms
from .models import Tarefa

from urllib import request


# Create your views here.
def lista_tarefas(request):
    lista_tarefas = Tarefa.objects.all()
    # status = request.GET.get('status')
    # print(status)
    return render(request, 'lista/index.html', {'lista_tarefas': lista_tarefas})


class TarefasNew(CreateView):
    model = Tarefa
    form_class = ListaForms
    context_objects_name = "tarefas"
    template_name = 'lista/new.html'

    def get_success_url(self):
        return reverse('lista')

def delete(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    tarefa.delete()
    return redirect('lista')

def riscado(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    tarefa.status = True
    tarefa.save()
    return redirect('lista')

def nao_riscado(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    tarefa.status = False
    tarefa.save()
    return redirect('lista')
