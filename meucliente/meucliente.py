import grpc
import time
import random
from meuservico_pb2 import Requisicao
from meuservico_pb2_grpc import MeuservicoStub
import os


#channel = grpc.insecure_channel("localhost:50051")
#client = MeuservicoStub(channel)

server_host2 = os.getenv("VAR_MEUSERVICO_HOST", "localhost") # recebe na hora de executar o docker a variavel VAR_MEUSERVICO_HOST.
                                                             # Reverte para localhost se não encontrar.
channel = grpc.insecure_channel( f"{server_host2}:50051" ) # cria um channel que vai conectar no host do meuservico
client = MeuservicoStub(channel)

print(client.ehPrimo(Requisicao(id=random.randrange(1,500,1))))
print(client.ehPrimo(Requisicao(id=random.randrange(1,500,1))))

while True:
    print(client.ehPrimo(Requisicao(id=random.randrange(1,500,1))))
    time.sleep(1)
