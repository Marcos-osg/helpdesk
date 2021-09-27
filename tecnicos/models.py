from django.db import models
import uuid

# Create your models here.
class Tecnico(models.Model):
    ATIVO_CHOICES =[
        ('ATIVO','Ativo'),
        ('INATIVO','Inativo'),
    ]
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True,
        editable=False
    )
    nome = models.CharField(max_length=255,verbose_name='Nome do Tecnico')
    registro = models.CharField(max_length=20, verbose_name='Registro')
    ativo = models.CharField(choices=ATIVO_CHOICES, max_length=100, verbose_name='Status do Tecnico', default='ATIVO')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tecnico'
        verbose_name_plural = 'Tecnicos'