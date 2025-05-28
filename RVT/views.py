from rest_framework import viewsets
from .models import TipoElemento, UnidadMedida, Material, Costo, Elemento
from .serializers import (
    TipoElementoSerializer,
    UnidadMedidaSerializer,
    MaterialSerializer,
    CostoSerializer,
    ElementoSerializer,
)

class TipoElementoViewSet(viewsets.ModelViewSet):
    queryset = TipoElemento.objects.all()
    serializer_class = TipoElementoSerializer

class UnidadMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadMedida.objects.all()
    serializer_class = UnidadMedidaSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class CostoViewSet(viewsets.ModelViewSet):
    queryset = Costo.objects.all()
    serializer_class = CostoSerializer

class ElementoViewSet(viewsets.ModelViewSet):
    queryset = Elemento.objects.all()
    serializer_class = ElementoSerializer