from rest_framework import serializers
from api.models import *

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = "__all__"

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class ConfiguracaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuracao
        fields = "__all__"