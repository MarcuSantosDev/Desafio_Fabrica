from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import MarcaModelViewSet

router = DefaultRouter()
router.register(prefix="modelo", viewset=MarcaModelViewSet)

urlpatterns = [
   path("", include(router.urls)),
]