from django.db import models

class Condominio(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class CasaModel(models.Model):
    numero_casa = models.IntegerField()
    bloco = models.IntegerField()
    quantidade_quartos = models.IntegerField()
    quantidade_banheiros = models.IntegerField()
    area_lazer = models.BooleanField()
    disponivel = models.BooleanField()

    def __str__(self):
        return f'casa {self.numero_casa}'
    
    class Meta:
        verbose_name = "Casa"
        verbose_name_plural = "Casas"

class NegociacaoCasaModel(models.Model):
    numero_casa = models.IntegerField()
    bloco = models.IntegerField()
    alugar_casa = models.BooleanField()
    comprar_casa = models.BooleanField()
    
    def __str__(self):
        return f'negociacao - Casa[{self.casa_numero}]'
    class Meta:
        verbose_name = "negociacao"
        verbose_name_plural = "negociacoes"