from django.contrib import admin
from servicos.models import Servico


@admin.register(Servico)
class Servico(admin.ModelAdmin):
    list_display = ('descricao_servico','tipo_servico','data_servico','data_entrega', 'status', 'tecnico', 'cliente',)