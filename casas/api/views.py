from rest_framework.viewsets import ModelViewSet
from casas.models import Casa
from .serializers import CasaSerializer

class CasaViewSet(ModelViewSet):
    queryset = Casa.objects.all()
    serializer_class = CasaSerializer
