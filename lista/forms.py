
from django import forms

from .models import Tarefa

class ListaForms(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = [
            "titulo",
            "descricao",
            "categoria",
            "status",

        ]