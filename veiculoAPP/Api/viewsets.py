from .serializers import MarcaSerializer
from ..models import MarcaModel
from rest_framework.viewsets import ModelViewSet
import requests
from rest_framework.response import Response

''''class MarcaModelViewSet(ModelViewSet):
    queryset = MarcaModel.objects.all()
    serializer_class = MarcaSerializer

'''

class MarcaModelViewSet(ModelViewSet):   # se dar um post na rota desse viewset vai cadastrar todas as marcas no Banco de dados
    queryset = MarcaModel.objects.all()
    serializer_class = MarcaSerializer    
    
    def create(self, request):
        site = (f'https://parallelum.com.br/fipe/api/v1/carros/marcas')
        requisicao = requests.get(site)
        json = requisicao.json()
        
        marcasSalvas = []
        for item in json:
            codigo = item.get('codigo', '')
            nome = item.get('nome', '')

            dadosrecebidos = {
                "codigo": f"{codigo}",
                "nome": f"{nome}", 
            }
        
            meuserializer = MarcaSerializer(data=dadosrecebidos)
            if meuserializer.is_valid():
                meuserializer.save()
                marcasSalvas.append(meuserializer.data)
