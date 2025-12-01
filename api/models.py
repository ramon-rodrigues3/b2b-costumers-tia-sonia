from django.db import models

class Configuracao(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    valor = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    codigo_totvs = models.IntegerField(unique=True)
    codigo_bitrix = models.IntegerField(unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    codigo_cliente = models.IntegerField(unique=True)
    razao_social = models.CharField(max_length=200)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.razao_social