from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tipo-elemento', views.TipoElementoViewSet)
router.register(r'unidad-medida', views.UnidadMedidaViewSet)
router.register(r'material', views.MaterialViewSet)
router.register(r'costo', views.CostoViewSet)
router.register(r'elemento', views.ElementoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]