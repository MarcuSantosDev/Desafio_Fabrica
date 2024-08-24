from rest_framework.serializers import ModelSerializer
from ..models import MarcaModel, CarroModeloModel

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = MarcaModel
        fields = '__all__'


class CarroModelSerializer(ModelSerializer):
    class Meta:
        model = CarroModeloModel
        fields = '__all__'