from .serializers import MarcaSerializer
from ..models import MarcaModel
from rest_framework.viewsets import ModelViewSet

class MarcaModelViewSet(ModelViewSet):
    queryset = MarcaModel.objects.all()
    serializer_class = MarcaSerializer
