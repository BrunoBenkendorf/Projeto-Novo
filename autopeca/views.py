from rest_framework import viewsets
from django.shortcuts import render, redirect
from .forms import PecaForm  # Você deve ter criado isso no forms.py
from .models import Peca  # Supondo que o nome do seu modelo seja Peca
from .models import Categoria, Fabricante, Peca, Cliente, Pedido, ItemPedido
from .serializers import (
    CategoriaSerializer, FabricanteSerializer, PecaSerializer,
    ClienteSerializer, PedidoSerializer, ItemPedidoSerializer
)

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class FabricanteViewSet(viewsets.ModelViewSet):
    queryset = Fabricante.objects.all()
    serializer_class = FabricanteSerializer

class PecaViewSet(viewsets.ModelViewSet):
    queryset = Peca.objects.all()
    serializer_class = PecaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer

def home(request):
    pecas = Peca.objects.all().order_by('-data_cadastro') # Buscar todas as peças
    return render(request, 'HomePage.html', {'pecas': pecas})


def adicionar_peca(request):
    if request.method == 'POST':
        form = PecaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # redireciona para a home ou outra página
    else:
        form = PecaForm()
    
    return render(request, 'adicionar_peca.html', {'form': form})
