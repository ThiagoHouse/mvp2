from rest_framework.serializers import ModelSerializer

from anunciante.models import Anunciante


class AnuncianteSerializer(ModelSerializer):
    class Meta:
        model = Anunciante
        fields = ('nome','senha', 'email')