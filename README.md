# exampleMicroservice
Just a sample implementation of a microservice using Google RPC in Python.
Started in September 2021

Exercised developed from tutorial:
https://realpython.com/python-microservices-grpc/#example-implementation

Github Image descriptions:
 - jrkessl/servidorweb:1.0 - The first version. Worked until soft_unicode was deprecated and removed from Python library markupsafe.
 - jrkessl/servidorweb:1.1 - Fixes the previous' version bug by using the latest version of Flask Python library.

# Commit: (primeiro commit) Instrucao para o microservico "meuservico"

## instrução 1/2: como fazer funcionar do zero 

1. criar arquivo /protobufs/<nome do servico>.proto // Define a API do serviço.
2. criar arquivo <nome do servico>/requirements.txt 
3. criar, ativar e configurar o ambiente virtual:   
`python3 -m venv venv0`  
`source venv0/bin/activate`  (este comando é na pasta do projeto)  
`cd <nome do servico>`  
`python -m pip install -r requirements.txt`

4. gerar o código python:  
`python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/<nome do servico>.proto`

5. criar o arquivo cliente cliente.py
6. criar o arquivo servidor <nome do servico>.py
7. rodar o servidor: `python3 <nome do servico>.py` (lembrar de estar com o ambiente virtual ativado) e, em outra janela, rodar o cliente.

## instrução 2/2: como fazer funcionar o projeto baixado do github 

1. baixar o projeto
`git clone https://github.com/jrkessl/exampleMicroservice`
3. `cd exampleMicroservice`
4. `python3 -m venv venv0`
5. `source venv0/bin/activate`
6. `cd meuservico`
7. `python -m pip install -r requirements.txt`
8. rodar o servidor: `python3 meuservico.py`
### E se quiser rodar o cliente:
1. Abre outro prompt
2. Volta à pasta raiz do projeto `cd $HOME/exampleMicroservice`
3. `source venv0/bin/activate`
4. `cd meuservico` 
5. rodar o cliente: `python3 cliente.py` 
Considere ainda usar o outro microservico "meucliente".

# Commit: (segundo commit) Instrucao para a pagina web com Flask 

## instrução 1/2: como fazer funcionar do zero 

0. fazer git clone deste commit:  
https://devopscube.com/checkout-clone-specific-git-commit-id-sha/
1. crie a pasta "servidorweb" na raiz do projeto
2. crie o arquivo "servidorweb\requirements.txt"; o conteudo do arquivo esta no arquivo homonimo no Repositorio no Github;
3. habilitar o ambiente virtual. Na pasta do projeto (exampleMicroservices):  
`sudo apt-get update`  
`sudo apt-get upgrade`  
`sudo apt install python3.8-venv`  
`python3 -m venv venv0`  
`source venv0/bin/activate`  
4. instale os requerimentos:  
`python -m pip install -r servidorweb/requirements.txt`  
5. crie o arquivo servidorweb/servidorweb.py; o conteudo do arquivo esta no Repo;
6. crie o arquivo servidorweb/templates/homepage.html; o conteudo do arquivo esta no Repo;
7. gere o codigo do meuservido na pasta do servidorweb (exampleMicroservices/servidorweb):  
`python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/meuservico.proto`
8. rode o meuservico em outra janela. Em outra janela, faça:  
`cd exampleMicroservice`  
`source venv0/bin/activate`  
`cd meuservico/`  
`python meuservico.py`  
9. (de volta na janela anterior) rode a aplicacao Flask:  
`FLASK_APP=servidorweb.py flask run`  
10. teste (em uma terceira janela):  
`curl http://127.0.0.1:5000/`  
11. Vai dar pau pois neste commit em particular o meuservico está ouvindo na porta 50051 mas o servidorweb está buscando na porta 50052. Corrija isso na linha 17 do arquivo servidorweb.py e linha 51 do meuservico.py: de 50052 para 50051.

## instrução 2/2: como fazer funcionar o projeto baixado do github 

1. `git clone https://github.com/jrkessl/exampleMicroservice`  
2. `cd exampleMicroservice`  
3. instalar e habilitar ambiente virtual:  
`sudo apt-get update`  
`sudo apt-get upgrade`  
`sudo apt install python3.8-venv`  
`python3 -m venv venv0`  
`source venv0/bin/activate`  
4. python -m pip install -r servidorweb/requirements.txt
5. rodar o meuserviço:  
`cd meuservico/`  
`python meuservico.py`  
6. rodar o servidorweb. Em outro terminal:   
`cd exampleMicroservice/`  
`source venv0/bin/activate`  
`cd servidorweb/`  
`FLASK_APP=servidorweb.py flask run`  
7. testar o servidor web. Em outro terminal: `curl http://127.0.0.1:5000`
 
# Commit: (terceiro commit) Instrucao para dockerizar os serviços 

## instrução 1/2: como fazer funcionar do zero

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
`docker network create microservices`
5. construir imagem (rodar na pasta exampleMicroservice):
`docker build . -f meuservico/Dockerfile -t meuservico`
6. rodar
`docker run -p 127.0.0.1:50051:50051/tcp --network microservices --name meuservicoDns meuservico`
obs. se fosse pra rodar sem ser numa network e sem passar um dnsname para o microserviço:
`docker run -p 127.0.0.1:50051:50051/tcp meuservico`

Fazer o Docker do servidorweb
1. criar servidorweb/Dockerfile 
2. alterar o servidorweb.py, a partir da linha 15, para conectar no dns name do meuservico, e não mais no localhost:  
sai:
`server_host2 = os.getenv("what do this do?", "localhost")`
`channel2 = grpc.insecure_channel( f"{server_host2}:50052" )`
          entra:
`server_host2 = os.getenv("VAR_MEUSERVICO_HOST", "localhost") ` (recebe na hora de executar o docker a variavel VAR_MEUSERVICO_HOST. Reverte para localhost se não encontrar.)
`channel2 = grpc.insecure_channel( f"{server_host2}:50051" ) ` (cria um channel que vai conectar no host do meuservico)
3. `docker build . -f servidorweb/Dockerfile -t servidorweb`
4. `docker run -p 127.0.0.1:5000:5000/tcp --network microservices -e VAR_MEUSERVICO_HOST=meuservicoDns servidorweb`
    obs. Sem especificar a network nem passar a variável, seria: 
    `docker run -p 127.0.0.1:5000:5000/tcp servidorweb`


## instrução 2/2: como fazer funcionar do projeto baixado do github 

Preparação:
1. baixar o último commit (o commit entitulado: "Adicionando Docker: adicionando instruções de como dockerizar os micr...")
2. instalar Docker
3. criar network
`docker network create microservices`

Preparar e lançar container do meuservico
1. construir imagem (rodar na pasta exampleMicroservice):
`docker build . -f meuservico/Dockerfile -t meuservico`
2. rodar
`docker run -p 127.0.0.1:50051:50051/tcp --network microservices --name meuservicoDns meuservico`
obs. se fosse pra rodar sem ser numa network e sem passar um dnsname para o microserviço:
`docker run -p 127.0.0.1:50051:50051/tcp meuservico`

Preparar e lançar o container do servidorweb
1. `docker build . -f servidorweb/Dockerfile -t servidorweb`
2. `docker run -p 127.0.0.1:5000:5000/tcp --network microservices -e VAR_MEUSERVICO_HOST=meuservicoDns servidorweb`
obs. Sem especificar a network nem passar a variável, seria:
`docker run -p 127.0.0.1:5000:5000/tcp servidorweb`

# Commit Bonus: microservico extra "meucliente" 

Este microserviço extra apenas roda em loop e conecta no "meuservico" para testar conectividade.

##### instrução: como fazer funcionar manualmente
 - pegar os arquivos (git clone)
 - `cd exampleMicroservice`
 - `source venv0/bin/activate` (aqui supondo que você já criou este ambiente virtual, pois já está rodando o meuservico
 - Pegar alguns arquivos que o meucliente precisa pra rodar:
`cd meucliente`
`cp ../meuservico/meuservico_pb2.py .`
`cp ../meuservico/meuservico_pb2_grpc.py .`
 - Rodar
`python3 meucliente.py`

##### instrução: como fazer funcionar usando docker  

Preparação
 - apt-get update, upgrade
 - pegar arquivos
`git clone https://github.com/jrkessl/exampleMicroservice`
- instalar docker (e configurar docker pra rodar sem sudo)
- executar os steps pra dar build e run no microserviço "meuserviço":  
`docker network create microservices`
`docker build . -f meuservico/Dockerfile -t meuservico`
`docker run -p 127.0.0.1:50051:50051/tcp --network microservices --name meuservicoDns meuservico &`  
 - criar arquivo de execução: meucliente/meucliente.py  
 - criar arquivo Dockerfile  
 - criar arquivo requirements.txt  
 - build:
`docker build . -f meucliente/Dockerfile -t meucliente`
 - rodar o container:
`docker run --network microservices -e VAR_MEUSERVICO_HOST=meuservicoDns meucliente`
onde: `--network microservices` > identificar a network  
`-e VAR_MEUSERVICO_HOST=meuservicoDns` > passar o endereço do outro microserviço onde vamos conectar  
`meucliente` > nome da imagem que vamos rodar
  
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
  
# Commit: adicionando pytest para testar microservicos dentro dos seus containeres

Como funciona:
 - Foi adicionado um arquivo de teste dentro de cada container; 
 - Aplica-se o comando "pytest" no container e o pytest se encarrega de descobrir o arquivo de teste, 
   a função de teste, executá-la e jogar o resultado no standard output.  

Testando o microserviço "meuservico": 
Este commit adiciona/altera:
 ./meuservico/requirements.txt > adicionado o requerimento de pytest, última versão
 ./meuservico/test_meuservico.py > arquivo com testes na sintaxe do pytest (autoteste.py presente na pasta, mas obsoleto)
 ./servidorweb/requirements.txt > removida a especificação de versão do pytest, para usar a última versão.
 ./servidorweb/test_servidorweb.py > código do autoteste desse microserviço

Instruções:
- para rodar este teste/para rodar um comando no container (sem entrar nele):
 $ docker exec examplemicroservice_meuservicoDns_1 pytest
 $ docker exec examplemicroservice_servidorweb_1   pytest
 $ docker exec <nome do container>                 <comando>

- para entrar no container e então rodar qualquer coisa: 
 $ docker exec -it examplemicroservice_meuservicoDns_1  /bin/bash
 $ docker exec -it examplemicroservice_servidorweb_1    /bin/bash
 $ docker exec -it <nome do container>                  /bin/bash
 
# Commit: adicionando comandos de upload (push) das imagens Docker para o AWS ECR, usando AWS CLI
02/12/2021

Steps para upload no ECR (via AWS CLI):
 - build the image, e conferir que foi criada (e rodar pra testar, se for o caso):
 $ docker-compose build
 $ docker build . -f meucliente/Dockerfile -t meucliente
 $ docker images

 - instalar e configurar aws cli
 - autenticar no registry
 $ aws ecr get-login-password --region <REGIAO> | docker login --username AWS --password-stdin <NO. DA CONTA>.dkr.ecr.<REGIAO>.amazonaws.com
exemplo:
 $ aws ecr get-login-password --region sa-east-1 | docker login --username AWS --password-stdin 465271007900.dkr.ecr.sa-east-1.amazonaws.com

 - dar tag na imagem
 $ docker tag <NOME DA IMAGEM>:latest <NO. DA CONTA>.dkr.ecr.<REGIAO>.amazonaws.com/<NOME DA IMAGEM>:latest
 $ docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]
exemplo:
 $ docker tag servidorweb:latest 465271007900.dkr.ecr.sa-east-1.amazonaws.com/servidorweb:latest
 $ docker tag meuservico:latest  465271007900.dkr.ecr.sa-east-1.amazonaws.com/meuservico:latest
 $ docker tag meucliente:latest  465271007900.dkr.ecr.sa-east-1.amazonaws.com/meucliente:latest
- fazer push na imagem
 $ docker push <NO. DA CONTA>.dkr.ecr.<REGIAO>.amazonaws.com/<NOME DA IMAGEM>:latest
exemplo:
 $ docker push 465271007900.dkr.ecr.sa-east-1.amazonaws.com/servidorweb:latest
 $ docker push 465271007900.dkr.ecr.sa-east-1.amazonaws.com/meucliente:latest
 $ docker push 465271007900.dkr.ecr.sa-east-1.amazonaws.com/meuservico:latest

# Commit: adicionando comandos de download (pull) de imagens Docker do AWS ECR, usando AWS CLI
04/12/2021

Steps:
1. Instalar aws cli
2. fazer aws configure

3. Fazer docker login
 - aws ecr get-login-password --region <REGIAO> | docker login --username AWS --password-stdin <NO. DA CONTA>.dkr.ecr.<REGIAO>.amazonaws.com
 - aws ecr get-login-password --region sa-east-1 | docker login --username AWS --password-stdin 465271007900.dkr.ecr.sa-east-1.amazonaws.com

4. Pull
 - docker pull <NO. DA CONTA>.dkr.ecr.<REGIAO>.amazonaws.com/<NOME DA IMAGEM>:<TAG DA IMAGEM>
 - docker pull 465271007900.dkr.ecr.sa-east-1.amazonaws.com/meuservico:latest
 - docker pull 465271007900.dkr.ecr.sa-east-1.amazonaws.com/servidorweb:latest
 - docker pull 465271007900.dkr.ecr.sa-east-1.amazonaws.com/meucliente:latest

5. Rodar
 - docker run -p 127.0.0.1:5000:5000/tcp --network microservices -e VAR_MEUSERVICO_HOST=meuservicoDns 465271007900.dkr.ecr.sa-east-1.amazonaws.com/servidorweb
 - docker run -p 127.0.0.1:50051:50051/tcp --network microservices --name meuservicoDns 465271007900.dkr.ecr.sa-east-1.amazonaws.com/meuservico

# Commit: adding declarative kubernetes yaml file to deploy these containers in Kubernetes, instead of Docker Swarm  
Just check files deployMeuservicoMeucliente.yml and deployMeuservicoServidorweb.yml. It's all there.  

# Commit (feature added): helm  
Added a simple local helm chart, that deploys these services to the cluster using Helm.  
Usage:  considering the name of the helm release will be `meus`, go to the project's rool folder and do:  
`helm install meus helm/exampleMicroservice/`  
or:  
`helm upgrade --install -n qa meus helm/exampleMicroservice/`  
  
Change values in values.yaml file. Or, to set a value in the command line:  
`helm upgrade --install -n qa meus --set meuservico.tag=1.0 helm/exampleMicroservice/`  
  
# Commit (feature added): helm chart with ingress object, alb class  
Added a new helm chart that replaces the load balancer with an ingress object, class 'alb' (the AWS ingress controller). This is a new helm chart and the other one is still available. Install this chart with:  
`helm upgrade --install -n qa examic helm/exampleMicroservice-ingress-alb/`  
Delete with:  
`helm delete -n qa examic`  
Important: The host value(s) defined in the rules section of ingress definition file need DNS records created for them, before this complete solution works. They do not get automatically created. For those host value(s) you need to do either one of:  
 1. Choose host values in a domain you own, and where your DNS zone is hosted (Route 53?) create CNAME records for them, pointing to the address of the load balancer that will get created in AWS;
 2. After the load balancer gets created, resolve its address, get one of the IPs it will have at the time, and create aliases between that IP and the host values from ingress.yaml in your /etc/hosts file.  