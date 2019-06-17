from rest_framework.serializers import ModelSerializer
from enderecoEntrega.models import EnderecoEntrega

class EnderecoEntregaSerializer(ModelSerializer):
    class Meta:
        model = EnderecoEntrega
        fields = ('linha1','linha2', 'cidade', 'estado','pais')