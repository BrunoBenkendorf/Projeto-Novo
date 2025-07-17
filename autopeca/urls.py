from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoriaViewSet, FabricanteViewSet, PecaViewSet,
    ClienteViewSet, PedidoViewSet, ItemPedidoViewSet,
    home, adicionar_peca  # <-- você importou direto, então use direto
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
]
