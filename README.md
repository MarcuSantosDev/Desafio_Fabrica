Resumo breve do que irá ser abordado 📌
Consiste em ler os dados de uma api externa (https://parallelum.com.br/fipe/api/v1) e retornar uma Fipe de veiculos.

▪️Requerimentos 📋
Antes de tudo, é de suma importância ter o Python instalado, além de ser indispensável a criação de um ambiente virtual e a instalação de dependências essenciais.

py -m venv (nome da venv) - # Criação da venv com o nome desejado
.\(nome da venv)\Scripts\activate - # Comando para entrar na venv; Caso ocorra bloqueio ⛔, utlize 'Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass'
Ademais, instale as seguintes dependências:

pip install django djangorestframework
pip install requests
Como acessar a API 🖥️
Em seu terminal, certifique-se de realizar, dentro da venv, os seguintes comandos:

py manage.py makemigrations
py manage.py migrate
Em seguida, para abrir o servidor local, use:

py manage.py runserver
Ao realizar o runserver, um IP local será definido (http://127.0.0.1:8000/), com isso, deve-se adicionar o encaminhamento correto http://127.0.0.1:8000/api/ip/

▪️SERIALIZERS: 
=> Filtro dos dados : O serializers irá filtrar os dados requeridos :

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = MarcaModel
        fields = '__all__'


class CarroModelSerializer(ModelSerializer):
    class Meta:
        model = CarroModeloModel
        fields = '__all__'

▪️VIEWSET:

==> ✏️ Se dar um post rota abaixo dessa viewset, irá cadastrar todas as marcas no Banco de dados :

class MarcaModelViewSet(ModelViewSet):   
    queryset = MarcaModel.objects.all()
    serializer_class = MarcaSerializer

==> ✅ Verificação de dados requeridos e gerar notificações :

for item in json:
            codigo = item.get('codigo')
            nome = item.get('nome')

            dadosrecebidos = {
                "codigo": f"{codigo}",
                "nome": f"{nome}", 
            }
        
            meuserializer = MarcaSerializer(data=dadosrecebidos)
            if meuserializer.is_valid():         verifica se o serializers é valido, se for valido volta True
                meuserializer.save()# salva no bd
                marcasSalvas.append(meuserializer.data)
            else:
                return Response(meuserializer.errors, status=status.HTTP_400_BAD_REQUEST) ❌ Erro no servidor devido a um erro do cliente
            
            return Response(meuserializer.data, status=status.HTTP_201_CREATED)   ✅  solicitação de recurso bem-sucedida


