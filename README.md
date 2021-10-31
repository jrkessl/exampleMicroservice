# exampleMicroservice
Just a sample implementation of a microservice using Google RPC in Python.
Started in September 2021

Exercised developed from tutorial:
https://realpython.com/python-microservices-grpc/#example-implementation

The first commit: 5ea9211e08595767cfd37c9583893d6874af2fd0
Is just a microservice "meuservico".

The second commit: 5c413c6907f6b3db69d918b7c3ade5e83b73b963
Adds a Flask web page that calls "meuservico" and displays results in the web page.

Instrucoes de como fazer funcionar esse projeto. 

Artigo de origem: 
https://realpython.com/python-microservices-grpc/#example-implementation

'****************************************************************************************
'****************************************************************************************
'***** (primeiro commit) Instrucao para o microservico "meuservico" *********************
'****************************************************************************************
'****************************************************************************************

'********************* instrução 1/2: como fazer funcionar do zero **********************

1. criar arquivo /protobufs/<nome do servico>.proto // Define a API do serviço.
2. criar arquivo <nome do servico>/requirements.txt 
3. criar, ativar e configurar o ambiente virtual: 
python3 -m venv venv0
source venv0/bin/activate  
    (o comando acima é na pasta do projeto)
cd <nome do servico>
python -m pip install -r requirements.txt

4. gerar o código python:
python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/<nome do servico>.proto

5. criar o arquivo cliente cliente.py
6. criar o arquivo servidor <nome do servico>.py
7. rodar o servidor: python3 <nome do servico>.py (lembrar de estar com o ambiente virtual ativado) e, em outra janela, rodar o cliente.

'********************* instrução 2/2: como fazer funcionar o projeto baixado do github *******************

1. baixar o projeto (com git clone)
2. cd exampleMicroservice
3. python3 -m venv venv0
4. source venv0/bin/activate  
5. cd meuservico
6. python -m pip install -r requirements.txt
7. rodar o servidor: python3 meuservico.py
8. voltar à pasta raiz do projeto (exampleMicroservices) e repetir a partir step 4 e 5 pra rodar o cliente
9. rodar o cliente: python3 cliente.py 

'****************************************************************************************
'****************************************************************************************
'****** (segundo commit) Instrucao para a pagina web com Flask **************************
'****************************************************************************************
'****************************************************************************************

'********************* instrução 1/2: como fazer funcionar do zero **********************

0. fazer git clone deste commit:
https://devopscube.com/checkout-clone-specific-git-commit-id-sha/
1. crie a pasta "servidorweb" na raiz do projeto
2. crie o arquivo "servidorweb\requirements.txt"; o conteudo do arquivo esta no arquivo homonimo no Repositorio no Github;
3. habilitar o ambiente virtual. Na pasta do projeto (exampleMicroservices):
 $ sudo apt-get update
 $ sudo apt-get upgrade
 $ sudo apt install python3.8-venv
 $ python3 -m venv venv0
 $ source venv0/bin/activate
4. instale os requerimentos:
 $ python -m pip install -r servidorweb/requirements.txt
5. crie o arquivo servidorweb/servidorweb.py; o conteudo do arquivo esta no Repo;
6. crie o arquivo servidorweb/templates/homepage.html; o conteudo do arquivo esta no Repo;
7. gere o codigo do meuservido na pasta do servidorweb (exampleMicroservices/servidorweb):
 $ python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/meuservico.proto
8. rode o meuservico em outra janela. Em outra janela, faça:
 $ cd exampleMicroservice
 $ source venv0/bin/activate
 $ cd meuservico/
 $ python meuservico.py
9. (de volta na janela anterior) rode a aplicacao Flask:
 $ FLASK_APP=servidorweb.py flask run
10. teste (em uma terceira janela):
 $ curl http://127.0.0.1:5000/
11. Vai dar pau pois neste commit em particular o meuservico está ouvindo na porta 50051 mas o servidorweb está buscando na porta 50052. Corrija 
    isso na linha 17 do arquivo servidorweb.py e linha 51 do meuservico.py: de 50052 para 50051.

'********************* instrução 2/2: como fazer funcionar o projeto baixado do github *******************

1. git clone https://github.com/jrkessl/exampleMicroservice
2. cd exampleMicroservice
3. instalar e habilitar ambiente virtual:
 $ sudo apt-get update
 $ sudo apt-get upgrade
 $ sudo apt install python3.8-venv
 $ python3 -m venv venv0
 $ source venv0/bin/activate
4. python -m pip install -r servidorweb/requirements.txt
5. rodar o meuserviço:
 $ cd meuservico/
 $ python meuservico.py
6. rodar o servidorweb. Em outro terminal: 
 $ cd exampleMicroservice/
 $ source venv0/bin/activate
 $ cd servidorweb/
 $ FLASK_APP=servidorweb.py flask run
7. testar o servidor web. Em outro terminal: $ curl http://127.0.0.1:5000
 

'****************************************************************************************
'****************************************************************************************
'****** (terceiro commit) Instrucao para dockerizar os serviços *************************
'****************************************************************************************
'****************************************************************************************

'********************* instrução 1/2: como fazer funcionar do zero **********************

Preparação
1. corrigir a porta usada pelo meuservico para parar de dar confusão. Substituir a porta 50052 por 50051 em:
 - linha 17 do arquivo servidorweb.py
 - linha 51 do meuservico.py
 - também no cliente.py se for usá-lo.  

Fazer o Docker do meuservico
1. git clone https://github.com/jrkessl/exampleMicroservice
2. criar meuservico/Dockerfile 
3. instalar Docker
4. criar network
 $ docker network create microservices
5. construir imagem (rodar na pasta exampleMicroservice):
 $ docker build . -f meuservico/Dockerfile -t meuservico
6. rodar
 $ docker run -p 127.0.0.1:50051:50051/tcp --network microservices --name meuservicoDns meuservico
    obs. se fosse pra rodar sem ser numa network e sem passar um dnsname para o microserviço:
     $ docker run -p 127.0.0.1:50051:50051/tcp meuservico

Fazer o Docker do servidorweb
1. criar servidorweb/Dockerfile 
2. alterar o servidorweb.py, a partir da linha 15, para conectar no dns name do meuservico, e não mais no localhost:
          sai:
              #server_host2 = os.getenv("what do this do?22", "localhost")
              #channel2 = grpc.insecure_channel( f"{server_host2}:50052" )
          entra:
              server_host2 = os.getenv("VAR_MEUSERVICO_HOST", "localhost") # recebe na hora de executar o docker a variavel VAR_MEUSERVICO_HOST.
                                                                           # Reverte para localhost se não encontrar.
              channel2 = grpc.insecure_channel( f"{server_host2}:50051" ) # cria um channel que vai conectar no host do meuservico
3. docker build . -f servidorweb/Dockerfile -t servidorweb
4. docker run -p 127.0.0.1:5000:5000/tcp --network microservices -e VAR_MEUSERVICO_HOST=meuservicoDns servidorweb
    obs. Sem especificar a network nem passar a variável, seria: $ docker run -p 127.0.0.1:5000:5000/tcp servidorweb


'********************* instrução 2/2: como fazer funcionar do projeto baixado do github **********************

Preparação:
1. baixar o último commit (o commit entitulado: "Adicionando Docker: adicionando instruções de como dockerizar os micr...")
2. instalar Docker
3. criar network
 $ docker network create microservices

Preparar e lançar container do meuservico
1. construir imagem (rodar na pasta exampleMicroservice):
 $ docker build . -f meuservico/Dockerfile -t meuservico
2. rodar
 $ docker run -p 127.0.0.1:50051:50051/tcp --network microservices --name meuservicoDns meuservico
    obs. se fosse pra rodar sem ser numa network e sem passar um dnsname para o microserviço:
     $ docker run -p 127.0.0.1:50051:50051/tcp meuservico

Preparar e lançar o container do servidorweb
1. docker build . -f servidorweb/Dockerfile -t servidorweb
2. docker run -p 127.0.0.1:5000:5000/tcp --network microservices -e VAR_MEUSERVICO_HOST=meuservicoDns servidorweb
    obs. Sem especificar a network nem passar a variável, seria: $ docker run -p 127.0.0.1:5000:5000/tcp servidorweb

# Commit Bonus: microservico extra "meucliente" 

Este microserviço extra apenas roda em loop e conecta no "meuservico" para testar conectividade.

##### instrução: como fazer funcionar (seja criando do zero, seja baixando do github) 

Preparação
 -apt-get update, upgrade
 -git clone https://github.com/jrkessl/exampleMicroservice
 -instalar docker
 -configurar docker pra rodar sem sudo
 -nano $HOME/.nanorc
 -executar os steps pra dar build e run no microserviço "meuserviço":
  $ docker network create microservices
  $ docker build . -f meuservico/Dockerfile -t meuservico
  $ docker run -p 127.0.0.1:50051:50051/tcp --network microservices --name meuservicoDns meuservico &
1.criar arquivo de execução: meucliente/meucliente.py
2.criar arquivo Dockerfile
3.criar arquivo requirements.txt
4.build: $ docker build . -f meucliente/Dockerfile -t meucliente
5.rodar o container: $ docker run --network microservices -e VAR_MEUSERVICO_HOST=meuservicoDns meucliente
	onde: --network microservices > identificar a network
	      -e VAR_MEUSERVICO_HOST=meuservicoDns > passar o endereço do outro microserviço onde vamos conectar
	      meucliente > nome da imagem que vamos rodar, eu acho

# Commit: adicionando docker compose

Só adicionando o arquivo e a instrução de como executá-lo.
 -novo arquivo: docker-compose.yaml
Instruções de uso:
 $ docker-compose up       [só pra subir tudo, sem recriar imagens]
 $ docker-compose build    [pra criar ou recriar as imagens]

# Commit: bootstrapping e cloud-init

Este commit adiciona:
 ./cloud_init.yaml > script de bootstrapping com instruções de uso. 

# Commit: testando um microserviço por dentro

Este commit adiciona:
 ./meuservico/autoteste.py > arquivo que testa o microserviço

Instruções:
 $ docker-compose up                                                   [só pra subir tudo]
 $ docker exec -it examplemicroservice_meuservicoDns_1  /bin/bash      [entrar no container]
 $ python3 autoteste.py                                                [testar o container de dentro]
 $ cat log.txt                                                         [ver o resultado do teste]
