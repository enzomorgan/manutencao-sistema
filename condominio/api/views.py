import logging

from typing import Any
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from condominio.api.serializers import CondominioSerializer, CasaSerializer
from condominio.models import CondominioModel, CasaModel
#from usuarios.api.permissions import IsMorador

logger = logging.getLogger("condominios")

class CasaViewSet(ModelViewSet):
    serializer_class = CasaSerializer
    permission_classes = [AllowAny]
    queryset = CasaModel.objects.all()

    def create(self, request):
        serializer = CasaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        numero = serializer.validated_data['numero']
        bloco = serializer.validated_data['bloco']

        in_database = CasaModel.objects.filter(numero=numero, bloco=bloco).exists()

        if not in_database:
            nova_casa = CasaModel.objects.create(
                numero=serializer.validated_data['numero'],
                bloco=serializer.validated_data['bloco'],
                capacidade=serializer.validated_data['capacidade'],
                tipo=serializer.validated_data['tipo'],
                disponivel=serializer.validated_data['disponivel']
            )

            serializer_saida = CasaSerializer(nova_casa)
            logger.info("Casa Criada!")
            return Response({"Info": "Casa criada!", "data": serializer_saida.data}, status=status.HTTP_201_CREATED)
        else:
            logger.error("A sala já está cadastrada.")
            return Response({"Info": "Falha ao tentar cadastrar a casa!"}, status=status.HTTP_409_CONFLICT)
        
    #from rest_framework.decorators import action
    #http://localhost:8000/casas/buscar/
    @action(methods=['get'],detail=False,url_path="buscar")
    def buscar_casa(self, request):
        busca = CasaModel.objects.filter(bloco=2)
        serializer = CasaSerializer(busca, many=True)
        return Response({"Info":"Lista de Casas", "data":serializer.data}, status=status.HTTP_200_OK)
    
    @action(methods=['delete'], detail=False, url_path="deletar")
    def deletar_casa(self, request):
        numero = request.query_params.get('numero', None)
        
        if numero is not None:
            try:
                casa = CasaModel.objects.get(numero=numero)
                casa.delete()  # Exclui a casa
                return Response({"Info": "Casa deletada com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
            except CasaModel.DoesNotExist:
                return Response({"Info": "Casa não encontrada!"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Info": "Número da casa não fornecido!"}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(methods=['get'], detail=False, url_path="listar")
    def listar_casas(self, request):
        casas = CasaModel.objects.all()  # Lista todas as casas
        serializer = CasaSerializer(casas, many=True)
        return Response({"Info": "Lista de Casas", "data": serializer.data}, status=status.HTTP_200_OK)    

class CondominioViewSet(ModelViewSet):
    serializer_class = CondominioSerializer
    permission_classes = [AllowAny]
    queryset = CondominioModel.objects.all()
    
    def create(self, request):
        serializer = CondominioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        casa_numero = serializer.validated_data['sala_numero']
        hora_inicio = serializer.validated_data['hora_inicio']
        hora_fim = serializer.validated_data['hora_fim']

        sala_existe = CasaModel.objects.filter(numero=casa_numero).exists()
        in_conflict = CondominioModel.objects.filter(casa_numero=casa_numero, hora_inicio__lt=hora_fim, hora_fim__gt=hora_inicio).exists()

        if sala_existe and not in_conflict:
            novo_condominio = CondominioModel.objects.create(
                casa_numero=serializer.validated_data['casa_numero'],
                hora_inicio=serializer.validated_data['hora_inicio'],
                hora_fim=serializer.validated_data['hora_fim']
            )

            serializer_saida = CondominioSerializer(novo_condominio)
            return Response({"Info": "Condominio cadastrado!", "data":serializer_saida.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"Info": "Falha ao tentar cadastrar o condominio!"},status=status.HTTP_409_CONFLICT)