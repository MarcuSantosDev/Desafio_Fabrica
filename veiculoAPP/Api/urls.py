from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import MarcaModelViewSet, CarroModeloModelViewSet

router = DefaultRouter()
router.register(prefix="marca", viewset=MarcaModelViewSet)  # rota para cadastrar as marcas no bd 
router.register(prefix="modelo", viewset=CarroModeloModelViewSet, basename="Modelos")# rota para cadastrar todos os modelos de acordo com a  no bd 

urlpatterns = [
   path("", include(router.urls)),
]