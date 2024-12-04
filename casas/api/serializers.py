from rest_framework import serializers
from casas.models import Casa
from condominio.models import CasaModel

class CasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casa
        fields = '__all__'

class CasaReserva(CasaModel):
    
    class Meta:
        model = CasaModel
        fields = "__all__"