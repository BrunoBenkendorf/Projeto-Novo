from django.db import models

# Categoria da peça (ex: Motor, Suspensão, Freio, etc.)
class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

# Fabricante da peça
class Fabricante(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    site = models.URLField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome

# Peça automotiva
class Peca(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.SET_NULL, null=True)
    imagem = models.ImageField(upload_to='pecas/', blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

# Cliente que realiza compras
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.TextField()

    def __str__(self):
        return self.nome

# Pedido de compra
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('Pendente', 'Pendente'),
        ('Enviado', 'Enviado'),
        ('Entregue', 'Entregue'),
        ('Cancelado', 'Cancelado'),
    ], default='Pendente')

    def __str__(self):
        return f'Pedido #{self.id} - {self.cliente.nome}'

# Itens do pedido
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    peca = models.ForeignKey(Peca, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.quantidade} x {self.peca.nome}'

    def subtotal(self):
        return self.quantidade * self.peca.preco
