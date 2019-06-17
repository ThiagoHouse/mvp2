from rest_framework.viewsets import ModelViewSet
from .serializers import EnderecoEntregaSerializer
from enderecoEntrega.models import EnderecoEntrega


class EnderecoEntregaViewSet(ModelViewSet):

    queryset = EnderecoEntrega.objects.all()
    serializer_class = EnderecoEntregaSerializer