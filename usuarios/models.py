from django.db import models

class Casa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
