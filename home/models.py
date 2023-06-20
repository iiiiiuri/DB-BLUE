from django.db import models


# Create your models here.


class contas(models.Model):
    id = models.AutoField(db_index=True, unique=True, primary_key=True)
    nome = models.CharField(max_length=15, verbose_name='Nome')
    sobrenome = models.CharField(max_length=15, verbose_name='Sobrenome')
    user = models.CharField(max_length=10, verbose_name='Usuario')
    senha = models.CharField(max_length=25, verbose_name='Senha')
    email = models.EmailField(max_length=25, verbose_name='Email')


class dados(models.Model):
    usuario = models.ForeignKey(contas, on_delete=models.CASCADE, verbose_name='Nome')
    dados = models.FileField(upload_to='Arquivos', max_length=100, verbose_name='Dados')


        