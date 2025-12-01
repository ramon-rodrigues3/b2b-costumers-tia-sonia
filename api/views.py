from rest_framework import generics, viewsets
from api.models import Vendedor, Cliente, Configuracao
from api.serializers import VendedorSerializer, ClienteSerializer, ConfiguracaoSerializer

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ConfiguracaoViewSet(viewsets.ModelViewSet):
    queryset = Configuracao.objects.all()
    serializer_class = ConfiguracaoSerializer