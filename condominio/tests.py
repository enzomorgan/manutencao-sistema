from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from condominio.models import CasaModel

# Create your tests here.

class CasaTesteCase(TestCase):

    def setUp(self):
        pass

    def test_cadastrar_cala(self):
        url = "http://localhost:8000/casas/"
        data = {
            "numero": 2,
            "bloco": 2,
            "capacidade": 5,
            "tipo": "Casa",
            "disponivel": True
        }
        response = self.client.post(url,data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CasaModel.objects.filter(numero=2,bloco=2).exists())

        response = self.client.post(url,data)
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
    
    def test_listar_calas(self):
        url = "http://localhost:8000/casas/"
        CasaModel.objects.create(
            numero=3,
            bloco=1,
            capacidade=3,
            tipo="Apto",
            disponivel=True
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['numero'],3)

