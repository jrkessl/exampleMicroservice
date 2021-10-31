import grpc
import random
import sys
from meuservico_pb2 import Requisicao
from meuservico_pb2_grpc import MeuservicoStub
from datetime import datetime

channel = grpc.insecure_channel("localhost:50051")
client = MeuservicoStub(channel)

with open("./log.txt", "w") as f:
    #f.write("\n")
    f.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " Nova execução (obs. log limpo a cada execução)\n")

resp1 = client.ehPrimo(Requisicao(id=1))
i = resp1.texto.find("1 eh primo")
if i == -1:
    with open("./log.txt", "a") as f:
        f.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " ERRO: teste de se 1 é primo falhou; i=" + str(i) + "\n")
        f.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " FALHOU\n")
    sys.exit()

resp1 = client.ehPrimo(Requisicao(id=4))
i = resp1.texto.find("4 NAO eh primo")
if i == -1:
    with open("./log.txt", "a") as f:
        f.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " ERRO: teste de se 4 é primo falhou; i=" + str(i) + "\n")
        f.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " FALHOU\n")
    sys.exit()

with open("./log.txt", "a") as f:
    f.write(datetime.now().strftime("%m/%d/%Y, %H:%M:%S") + " PASSOU\n")

