from django.db import models

# Create your models here.


class contas(models.Model):
    nome = models.CharField(max_length=15)
    sobrenome = models.CharField(max_length=15)
    user = models.CharField(max_length=10)
    senha = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)


class dados(models.Model):
    usuario = models.ForeignKey(contas, on_delete=models.CASCADE)
    dados = models.FileField(upload_to='Arquivos', max_length=100)