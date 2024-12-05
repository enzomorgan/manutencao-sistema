from django.db import models

# Create your models here.

class CasaModel(models.Model):

    numero = models.IntegerField()
    bloco = models.IntegerField()
    quantidade_quartos = models.IntegerField(default=0)
    quantidade_banheiros = models.IntegerField(default=0)
    area_lazer = models.BooleanField(default=False)
    garagem = models.BooleanField(default=False)
    disponivel = models.BooleanField(default=False)

    def __str__(self):
        return f'Casa {self.numero}'
    
    class Meta:
        verbose_name = "Casa"
        verbose_name_plural = "Casas"

class CondominioModel(models.Model):
    casa_numero = models.IntegerField()
    endereco = models.CharField(max_length=250, default="Endereço não especificado")


    def __str__(self):
        return f'Condominio - Casa[{self.casa_numero}] - [{self.endereco}]'
    
    class Meta:
        verbose_name = "Condomínio"
        verbose_name_plural = "Condomínios"
