
from django import forms

from .models import Tarefa

class ListaForms(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = [
            "descricao",
            "categoria",
            "status",
        ]