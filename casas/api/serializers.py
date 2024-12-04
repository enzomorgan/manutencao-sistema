from rest_framework import serializers
from casas.models import Casa

class CasaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Casa
        fields = '__all__'
