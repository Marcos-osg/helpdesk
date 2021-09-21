from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


class Cliente(models.Model):
    ESTADO_CHOICES=[
        ('AC','Acre'),
        ('AL','Alagoas'),
        ('AM','Amazonas'),
        ('AP','Amapá'),
        ('BA','Bahia'),
        ('CE','Ceará'),
        ('DF','Distrito Federal'),
        ('ES','Espírito Santo'),
        ('GO','Goiás'),
        ('MA','Maranhão'),
        ('MG','Minas Gerais'),
        ('MS','Mato Grosso do Sul'),
        ('MT','Mato Grosso'),
        ('PA','Pará'),
        ('PB','Paraíba'),
        ('PE','Pernambuco'),
        ('PI','Piauí'),
        ('PR','Paraná'),
        ('RJ','Rio de Janeiro'),
        ('RN','Rio Grande do Norte'),
        ('RO','Rondônia'),
        ('RR','Roraima'),
        ('RS','Rio Grande do Sul'),
        ('SC','Santa Catarina'),
        ('SE','Sergipe'),
        ('SP','São Paulo'),
        ('TO','Tocantins'),
    ]
    nome_completo = models.CharField(max_length=255, verbose_name="Nome do cliente")
    cpf = models.CharField(max_length=11 ,unique=True, verbose_name='CPF')
    telefone = models.CharField(max_length=11, null=True, blank=True)
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    estado = models.CharField(choices=ESTADO_CHOICES,max_length=255, verbose_name='Estado')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome_completo