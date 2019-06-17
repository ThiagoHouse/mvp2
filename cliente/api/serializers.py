from rest_framework.serializers import ModelSerializer

from cliente.models import Cliente


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nome','telefone', 'email')