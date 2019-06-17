from rest_framework.viewsets import ModelViewSet

from pecas.models import Pecas
from .serializers import PecasSerializer

class PecasViewSet(ModelViewSet):

    queryset = Pecas.objects.all()
    serializer_class = PecasSerializer