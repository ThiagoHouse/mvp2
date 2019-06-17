from rest_framework.viewsets import ModelViewSet
from anunciante.models import Anunciante
from .serializers import AnuncianteSerializer

class AnucianteViewSet(ModelViewSet):

    queryset = Anunciante.objects.all()
    serializer_class = AnuncianteSerializer