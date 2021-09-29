from django.db import models
import uuid

# Create your models here.
class Produto(models.Model):
    DISPONIVEL_CHOICES = [
        ('Sim','Sim'),
        ('Nao','Não'),
    ]
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True,
        editable=False
    )
    item = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.FloatField()
    disponivel = models.CharField(max_length=10, choices=DISPONIVEL_CHOICES, default='Nao')

    def __str__(self):
        return self.item

    class Meta:
        ordering = ['-disponivel']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'