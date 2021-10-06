import grpc
import random
from meuservico_pb2 import Requisicao
from meuservico_pb2_grpc import MeuservicoStub



channel = grpc.insecure_channel("localhost:50051")
client = MeuservicoStub(channel)

req = Requisicao(
    id=9
)

print("client.chamada1(requisicao):")
print(client.chamada1(req))

print("client.chamada2(requisicao):")
print(client.chamada2(req))

print("client.ehPrimo(Requisicao(id=random.randrange(1,50,1))))")
print(client.ehPrimo(Requisicao(id=random.randrange(1,50,1))))
