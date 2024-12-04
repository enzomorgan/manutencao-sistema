from django.db import models
from condominio.models import Condominio
from django.contrib.auth.models import User

class Casa(models.Model):
    numero = models.CharField(max_length=10)
    condominio = models.ForeignKey(Condominio, on_delete=models.CASCADE, related_name="casas")
    morador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Casa {self.numero} - {self.condominio.nome}"
