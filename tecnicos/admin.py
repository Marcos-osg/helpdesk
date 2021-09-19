from django.contrib import admin
from tecnicos.models import Tecnico


@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'registro',)
    