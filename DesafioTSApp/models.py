from builtins import max
from django.db import models
from django.utils import timezone

# Create your models here.
class Solicitante(models.Model):
    Nome = models.TextField(max_length=150)
    Email = models.EmailField(max_length=65)
    Telefone = models.TextField(max_length=30)
    CPF = models.TextField(max_length=14)

    def __str__(self):
        return self.Nome




class Teleconsultor(models.Model):
    Nome = models.TextField(max_length=150)
    Email = models.EmailField(max_length=65)
    CRM = models.TextField(max_length=10)
    DataFormatura = models.DateField()


class Solicitacao(models.Model):
    Texto = models.TextField(max_length=1000)
    solicitante = models.ForeignKey(Solicitante)
    DataSolicitacao = models.DateTimeField(default=timezone.now())




