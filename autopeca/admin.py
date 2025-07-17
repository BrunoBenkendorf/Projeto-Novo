from django.contrib import admin
from .models import Categoria, Fabricante, Peca, Cliente, Pedido, ItemPedido

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']

@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'site']
    search_fields = ['nome']

@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'estoque', 'categoria', 'fabricante']
    list_filter = ['categoria', 'fabricante']
    search_fields = ['nome', 'descricao']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'telefone']
    search_fields = ['nome', 'email']

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'data_pedido', 'status']
    list_filter = ['status']
    inlines = [ItemPedidoInline]
