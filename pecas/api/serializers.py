from rest_framework.serializers import ModelSerializer
from pecas.models import Pecas


class PecasSerializer(ModelSerializer):
    class Meta:
        model = Pecas
        fields = ('nome','descricao', 'preco')