from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'