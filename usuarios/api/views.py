from django.contrib.auth.models import User, Group
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from usuarios.api.serializers import MoradorCreateSerializer, MoradorSerializer, UserProfileExampleSerializer

from usuarios.models import Morador, UserProfileExample

class UserProfileExampleViewSet(ModelViewSet):
    serializer_class = UserProfileExampleSerializer
    permission_classes = [AllowAny]
    queryset = UserProfileExample.objects.all()
    http_method_names = ['get', 'put']

class MoradorViewSet(ModelViewSet):
    serializer_class = MoradorSerializer
    permission_classes = [AllowAny]
    queryset = Morador.objects.all()

    def create(self, request):
        serializer = MoradorCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        novo_user = User.objects.create_user(
            username=serializer.validated_data['login'],
            password=serializer.validated_data['senha'],
        )
        grupo_moradores = Group.objects.get(name="Moradores")
        novo_user.groups.add(grupo_moradores)

        novo_morador = Morador.objects.create(
            nome=serializer.validated_data['nome'],
            cpf=serializer.validated_data['cpf'],
            telefone=serializer.validated_data['telefone'],
            user=novo_user
        )

        serializer_saida = MoradorSerializer(novo_morador)
        return Response({"Info": "Cadastro realizado!", "data":serializer_saida.data}, status=status.HTTP_201_CREATED)