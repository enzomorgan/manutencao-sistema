from rest_framework import serializers
from usuarios.models import UserProfileExample, Corretor

class CorretorSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfileExample
        fields = ['id', 'address', 'phone_number', 'birth_date', 'user']

class CorretorCreateSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(max_length=140)
    cpf = serializers.CharField(max_length=16)
    enderoco = serializers.CharField(max_length=240)
    telefone = serializers.CharField(max_length=16)
    login = serializers.CharField(max_lenght=100)
    senha = serializers.CharField(max_lenght=100) 
    
class

