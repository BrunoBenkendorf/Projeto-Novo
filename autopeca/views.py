from rest_framework import viewsets
from django.shortcuts import render, redirect
from .forms import PecaForm,LoginClienteForm,LoginFuncionarioForm,CadastroClienteForm,CadastroFuncionarioForm  
from .models import Categoria, Fabricante, Peca, Cliente, Pedido, ItemPedido,Funcionario
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
def cadastro_cliente(request):
    if request.method == 'POST':
        form = CadastroClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_cliente')  # redireciona após o cadastro
    else:
        form = CadastroClienteForm()
    return render(request, 'cadastro_cliente.html', {'form': form})


def cadastro_funcionario(request):
    if request.method == 'POST':
        form = CadastroFuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_funcionario')
    else:
        form = CadastroFuncionarioForm()
    return render(request, 'cadastro_funcionario.html', {'form': form})
def login_cliente(request):
    if request.method == 'POST':
        form = LoginClienteForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            try:
                cliente = Cliente.objects.get(email=email, senha=senha)
                request.session['cliente_id'] = cliente.id
                return redirect('home')  # Redirecione para a área do cliente
            except Cliente.DoesNotExist:
                form.add_error(None, 'Email ou senha inválidos.')
    else:
        form = LoginClienteForm()
    
    return render(request, 'login_cliente.html', {'form': form})


def login_funcionario(request):
    if request.method == 'POST':
        form = LoginFuncionarioForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            try:
                funcionario = Funcionario.objects.get(email=email, senha=senha)
                request.session['funcionario_id'] = funcionario.id
                return redirect('dashboard_funcionario')  # Redirecione para o painel do funcionário
            except Funcionario.DoesNotExist:
                form.add_error(None, 'Email ou senha inválidos.')
    else:
        form = LoginFuncionarioForm()
    
    return render(request, 'login_funcionario.html', {'form': form})