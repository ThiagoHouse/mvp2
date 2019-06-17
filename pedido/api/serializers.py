from rest_framework.serializers import ModelSerializer
from pedido.models import Pedido


class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = ('pecas','descricaoPeca', 'clientes','enderecoEntrega')