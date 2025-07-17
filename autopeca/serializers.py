from rest_framework import serializers
from .models import Categoria, Fabricante, Peca, Cliente, Pedido, ItemPedido

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class FabricanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fabricante
        fields = '__all__'

class PecaSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    fabricante = FabricanteSerializer(read_only=True)

    class Meta:
        model = Peca
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ItemPedidoSerializer(serializers.ModelSerializer):
    peca = PecaSerializer(read_only=True)

    class Meta:
        model = ItemPedido
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    itens = ItemPedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = '__all__'
