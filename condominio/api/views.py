from rest_framework import viewsets
from .models import Condominio
from .serializers import CondominioSerializer

class CondominioViewSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer
