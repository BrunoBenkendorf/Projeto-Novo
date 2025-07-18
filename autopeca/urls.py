from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoriaViewSet, FabricanteViewSet, PecaViewSet,
    ClienteViewSet, PedidoViewSet, ItemPedidoViewSet,
    home, adicionar_peca, login_cliente,login_funcionario,cadastro_cliente,cadastro_funcionario 
)

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'fabricantes', FabricanteViewSet)
router.register(r'pecas', PecaViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'itens-pedido', ItemPedidoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('home', home, name='home'),
    path('adicionar/', adicionar_peca, name='adicionar_peca'),
    path('cadastro/cliente/', cadastro_cliente, name='cadastro_cliente'),
    path('cadastro/funcionario/', cadastro_funcionario, name='cadastro_funcionario'),
    path('login/cliente/', login_cliente, name='login_cliente'),
    path('login/funcionario/', login_funcionario, name='login_funcionario'),
]
