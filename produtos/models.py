from django.db import models

# Create your models here.
class Produto(models.Model):
    DISPONIVEL_CHOICES = [
        ('sim','Sim'),
        ('nao','Não'),
    ]
    item = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    disponivel = models.CharField(max_length=10, choices=DISPONIVEL_CHOICES)

    def __str__(self):
        return self.item

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'