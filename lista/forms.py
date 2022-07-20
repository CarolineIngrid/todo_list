
from django import forms

from .models import Tarefa

class ListaForms(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = (
            'titulo',
            'descricao',
            'categoria',
            'status',
        )

        widget = {
            'titulo': forms.TextInput(attrs={'class': 'form-control',
                                             'placeholder': 'Adicione um nome a tarefa. Ex: Arrumar o quarto.'}),
            'descricao': forms.TextInput(attrs={'class':
                                                    'form-control',
                                                'placeholder':
                                                    'Deixe-a mais específica. Ex: Deixar tudo organizado. '
                                                    'Principalmente embaixo da cama!'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Textarea(attrs={'class': 'form-control'}),
        }