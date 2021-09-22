import uuid
from django.db import models
from tecnicos.models import Tecnico
from produtos.models import Produto
from accounts.models import Cliente
import uuid


# Create your models here.
class Servico(models.Model):
    TIPO_SERVICO_CHOICES = [
        ('Manutenção','Manutenção'),
        ('Troca','Troca'),
        ('Formatacao','Formatação'),
        ('Backup','Backup'),
    ]
    STATUS_CHOICES = [
        ('Nao finalizado', 'Não Finalizado'),
        ('Finalizado', 'Finalizado'),
    ]
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True,
        editable=False
    )
    descricao_servico = models.TextField(verbose_name='Descrição do Serviço')
    tipo_servico = models.CharField(choices=TIPO_SERVICO_CHOICES, verbose_name='Tipo de Serviço', max_length=25)
    data_servico = models.DateField(auto_now=True, verbose_name='Data de Inicio')
    data_entrega = models.DateField(verbose_name='Data prevista')
    status = models.CharField(choices=STATUS_CHOICES, max_length=25)
    tecnico = models.ForeignKey(Tecnico, related_name='tecnico', on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey(Cliente, related_name='cliente', on_delete=models.DO_NOTHING)
    produto = models.ForeignKey(Produto, related_name='produto', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.tipo_servico 

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'