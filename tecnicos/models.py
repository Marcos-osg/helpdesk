from django.db import models

# Create your models here.
class Tecnico(models.Model):
    nome = models.CharField(max_length=255)
    registro = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tecnico'
        verbose_name_plural = 'Tecnicos'