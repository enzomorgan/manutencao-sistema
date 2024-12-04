from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from usuarios.api.serializers import CorretorCreateSerializer, CorretorSerializer, UserProfileExampleSerializer

from usuarios.models import Corretor, UserProfileExample

class UserProfileExampleViewSet(ModelViewSet):
    serializer_class = UserProfileExampleSerializer
    permission_classes = [AllowAny]
    queryset = UserProfileExample.objects.all()
    http_method_names = ['get', 'put']

class CorretorViewSet(ModelViewSet):
    serializer_class = CorretorSerializer
    permission_classes = [AllowAny]
    queryset = Corretor.objects.all()

def create(self, request):
        serializer = CorretorCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        novo_user = User.objects.create_user(
            username=serializer.validated_data['login'],
            password=serializer.validated_data['senha'],
        )

        novo_Corretor = Corretor.objects.create(
            nome=serializer.validated_data['nome'],
            matricula=serializer.validated_data['matricula'],
            departamento=serializer.validated_data['departamento'],
            user=novo_user
        )

        serializer_saida = CorretorSerializer(novo_Corretor)
        return Response({"Info": "Cadastro realizado!", "data":serializer_saida.data}, status=status.HTTP_201_CREATED)
    
def update(self, request, *args, **kwargs):
        corretor = self.get_object()
        serializer = CorretorCreateSerializer(data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)

        if 'login' in serializer.validated_data:
            corretor.user.username = serializer.validated_data['login']
            corretor.user.save()

        corretor.nome = serializer.validated_data['nome']
        corretor.matricula = serializer.validated_data['matricula']
        corretor.departamento = serializer.validated_data['departamento']
        corretor.save()

        serializer_saida = CorretorSerializer(corretor)
        return Response(
            {"Info": "Atualização realizada com sucesso!", "data": serializer_saida.data},
            status=status.HTTP_200_OK)
    
def destroy(self, request, *args, **kwargs):
        corretor = self.get_object()
        corretor.user.delete()  # Exclui o usuário associado
        corretor.delete()
        return Response({"Info": "Funcionário excluído com sucesso!"}, status=status.HTTP_204_NO_CONTENT)