from django.db import models

# Create your models here.

class CasaModel(models.Model):

    numero = models.IntegerField()
    bloco = models.IntegerField()
    quantidade_quartos = models.IntegerField()
    quantidade_banheiros = models.IntegerField()
    area_lazer = models.BooleanField()
    garagem = models.BooleanField()
    disponivel = models.BooleanField()

    def __str__(self):
        return f'Cala {self.numero}'
    
    class Meta:
        verbose_name = "Casa"
        verbose_name_plural = "Casas"

class CondominioModel(models.Model):
    casa_numero = models.IntegerField()
    endereco = models.CharField(max_length=250)

    def __str__(self):
        return f'Condominio - Casa[{self.sala_numero}] - [{self.hora_inicio}]'
    
    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"