from django.contrib import admin
from .models import Contato


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    # Colunas que aparecem na lista
    list_display = ('nome', 'usuario', 'telefone', 'cidade', 'estado')

    # Filtros laterais
    list_filter = ('estado', 'cidade', 'usuario')

    # Barra de pesquisa (busca por nome do contato ou nome do dono da agenda)
    search_fields = ('nome', 'email', 'usuario__username')

    # Paginação
    list_per_page = 20