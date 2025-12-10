from django.db import models

class Parametro(models.Model):
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
    class StatusImportacao(models.TextChoices):
        FATURADO = 'FT', 'Faturado'
        AGUARDANDO_FATURAMENTO = 'AF', 'Aguardando faturamento'
        NAO_REALIZADA = 'NR', 'Venda não realizada'
        AGUARDANDO_ATENDIMENTO = 'AA', 'Aguardando atendimento'
        AGUARDANDO_CADASTRO = 'AC', 'Aguardando cadastro'
        NAO_CADASTRADO = 'NC', 'Não cadastrado'
        CLIENTE_ATIVO_FORA = 'CA', 'Cliente ativo fora do CRM'
        FATURADO_FORA = 'FF', 'Faturado fora do CRM'

    codigo_cliente = models.IntegerField(unique=True)
    razao_social = models.CharField(max_length=200, null=True)
    cnpj_cpf = models.CharField(max_length=100, null=True)
    endereco = models.CharField(max_length=200, null=True)
    bairro = models.CharField(max_length=200, null=True)
    cidade = models.CharField(max_length=200, null=True)
    uf = models.CharField(max_length=50, null=True)
    telefone = models.CharField(max_length=100, null=True)
    email = models.TextField(null=True)
    vendedor = models.IntegerField(null=True)
    data_primeira_compra = models.DateField(null=True)
    data_ultima_compra = models.DateField(null=True)
    valor_ultima_compra = models.FloatField(null=True)
    produtos_ultima_compra = models.TextField(null=True)
    faturamento_acumulado = models.FloatField(default=0)
    qtd_pedidos = models.IntegerField(default=0)
    
    ultima_data_termino = models.DateField(null=True)
    status_importacao = models.CharField(max_length=2, choices=StatusImportacao.choices, null=True)
    periodicidade = models.IntegerField(null=True)
    responsavel_crm = models.IntegerField(null=True)
    id_contato = models.IntegerField(null=True)
    fantasia = models.CharField(max_length=200, null=True)
    data_atualizacao = models.DateField(null=True)

    def __str__(self):
        return self.razao_social