from django.contrib import admin
from produtos.models import Produto


@admin.register(Produto)
class Produto(admin.ModelAdmin):
    list_display = ('id','item','descricao', 'disponivel', 'valor',)