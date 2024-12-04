import logging
from rest_framework.viewsets import ModelViewSet
from casas.models import Casa
from rest_framework import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from casas.api.serializers import CasaSerializer
from casas.models import CasaModel

logger = logging.getLogger("casas")

class CasaViewSet(ModelViewSet):
    serializer_class = CasaSerializer
    permission_classes = [AllowAny]
    queryset = Casa.objects.all()

    def create(self, request):
        # Valida os dados recebidos e cria um novo objeto de serializer
        serializer = CasaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Obtém os dados validados
        numero = serializer.validated_data['numero']
        bloco = serializer.validated_data['bloco']

        # Verifica se já existe uma casa com o mesmo número e bloco
        in_database = CasaModel.objects.filter(numero=numero, bloco=bloco).exists()

        if not in_database:
            # Cria uma nova casa no banco de dados
            nova_casa = CasaModel.objects.create(
                numero_casa=serializer.validated_data['numero'],
                bloco=serializer.validated_data['bloco'],
                quantidade_quartos=serializer.validated_data['quartos'],  # Corrigido o nome do campo
                quantidade_banheiros=serializer.validated_data['banheiros'],
                area_lazer=serializer.validated_data['area_lazer'],  # Corrigido o erro de digitação
                disponivel=serializer.validated_data['disponivel']
            )

            # Serializa a casa criada para resposta
            serializer_saida = CasaSerializer(nova_casa)

            # Loga a criação bem-sucedida
            logger.info("Casa criada com sucesso!")

            # Retorna a resposta com status HTTP 201
            return Response({"Info": "Casa criada!", "data": serializer_saida.data}, status=status.HTTP_201_CREATED)
        else:
            # Loga o erro de tentativa de cadastro duplicado
            logger.error("A casa já está cadastrada.")

            # Retorna erro HTTP 409 de conflito
            return Response({"Info": "Falha ao tentar cadastrar a casa!"}, status=status.HTTP_409_CONFLICT)

    # Exemplo de como adicionar uma ação personalizada, comentado para referência futura
    # from rest_framework.decorators import action
    # @action(methods=['get'], detail=False, url_path="buscar")
    # def buscar_casa(self, request):
    #     busca = CasaModel.objects.filter(bloco=2)
    #     serializer = CasaSerializer(busca, many=True)
    #     return Response({"Info": "Lista de casas", "data": serializer.data}, status=status.HTTP_200_OK)
