from django.db import models
import uuid

# Create your models here.
class Tecnico(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True,
        editable=False
    )
    nome = models.CharField(max_length=255)
    registro = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Tecnico'
        verbose_name_plural = 'Tecnicos'