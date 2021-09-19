from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Servico(models.Model):
    TIPO_SERVICO_CHOICES = [
        ('manutenção','Manutenção'),
        ('troca','Troca'),
        ('formatação','Formatação'),
        ('backup','Backup'),
    ]
    descricao_servico = models.TextField(verbose_name='Descrição do Serviço')
    tipo_servico = models.CharField(choices=TIPO_SERVICO_CHOICES, verbose_name='Tipo de Serviço', max_length=25)

    def __str__(self):
        return self.tipo_servico

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'