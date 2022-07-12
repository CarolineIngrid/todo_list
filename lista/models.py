from django.db import models

# Create your models here.

class Tarefa(models.Model):
    # transformar em cores
    OPCAO_CATEGORIA = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('precisa ser feito', 'Precisa ser feito'),
    )


    descricao = models.CharField(max_length=400)
    criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=25, choices=OPCAO_CATEGORIA,
                                 default='importante')
    status = models.BooleanField(default=False)

