from rest_framework.viewsets import ModelViewSet
from pedido.models import Pedido
from .serializers import PedidoSerializer

class PedidoViewSet(ModelViewSet):

    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer