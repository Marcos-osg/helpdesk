from django.contrib import admin
from servicos.models import Servico


@admin.register(Servico)
class Servico(admin.ModelAdmin):
    list_display = ('descricao_servico','tipo_servico', 'valor', 'data_servico','data_entrega', 'status', 'tecnico', 'cliente',)