from rest_framework.serializers import ModelSerializer
from ..models import MarcaModel

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = MarcaModel
        fields = ['codigo', 'nome']