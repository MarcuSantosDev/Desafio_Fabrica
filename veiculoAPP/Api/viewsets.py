from .serializers import MarcaSerializer, CarroModelSerializer
from ..models import MarcaModel, CarroModeloModel
from rest_framework.viewsets import ModelViewSet
import requests
from rest_framework.response import Response
from rest_framework import status

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
            codigo = item.get('codigo')
            nome = item.get('nome')

            dadosrecebidos = {
                "codigo": f"{codigo}",
                "nome": f"{nome}", 
            }
        
            meuserializer = MarcaSerializer(data=dadosrecebidos)
            if meuserializer.is_valid():
                meuserializer.save()
                marcasSalvas.append(meuserializer.data)
    



class CarroModeloModelViewSet(ModelViewSet):
    queryset = CarroModeloModel.objects.all()
    serializer_class = CarroModelSerializer   # se dar um post na rota desse viewset vai cadastrar todas as marcas no Banco de dados
    def create(self, request):
        marca = request.data.get('marca')  # Usuário manda a marca no body
        if not marca:
            return Response({"detail": "Marca é necessária."}, status=status.HTTP_400_BAD_REQUEST)
        
        site = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca}/modelos'
        try:
            requisicao = requests.get(site)
            requisicao.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
            json_response = requisicao.json()    

            modelos_salvos = []

            modelos = json_response.get('modelos', [])  # Acessa a lista de modelos no JSON

            for item in modelos:
                codigo = item.get('codigo', '')
                nome = item.get('nome', '')

                dados_recebidos = {
                    "codigoMarca": marca,
                    "codigo": codigo,
                    "nome": nome,
                }

                serializer = self.serializer_class(data=dados_recebidos)
                if serializer.is_valid():
                    serializer.save()
                    modelos_salvos.append(serializer.data)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response(modelos_salvos, status=status.HTTP_201_CREATED)
        
        except requests.RequestException as e:
            return Response({"detail": "Erro na requisição para a API externa.", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except ValueError:
            return Response({"detail": "Erro ao processar a resposta da API externa."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)