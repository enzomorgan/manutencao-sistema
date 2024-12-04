from django.db import models

class Casa(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Corretor(models.Model):
     name = models.CharField(max_length=140, verbose_name= "Nome Completo")
     cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
     telefone = models.CharField(max_length=15, verbose_name="Telefone")

#status do corretor 
ativo = models.BooleanField(default=True, verbose_name="Ativo")

def __str__(self):
    return f'Corretor {self.nome} - CPF: {self.cpf}'

#Metodos
class Meta:
    verbose_name = 'Corretor'
    verbose_name_plural = 'Corretores'
