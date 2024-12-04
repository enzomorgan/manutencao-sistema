from rest_framework import serializers
from .models import Condominio # type: ignore

class CondominioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condominio
        fields = '__all__'
