from django.db import models

# Create your models here.

class Tarefa(models.Model):
    # transformar em cores
    OPCAO_CATEGORIA = (
        ('urgente', 'Urgente'),
        ('moderada', 'Moderada'),
        ('a fazer', 'A fazer'),
    )

    titulo = models.CharField(default='', max_length=24, blank=True)
    descricao = models.CharField(max_length=300)
    criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=25, choices=OPCAO_CATEGORIA, default='importante')
    status = models.BooleanField(default=False)

    def __str__(self):
        identidade = f'{self.descricao} {self.id}'
        return identidade


