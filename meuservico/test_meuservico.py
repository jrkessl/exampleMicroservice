#coding:utf-8
import grpc
import random
import sys
from meuservico_pb2 import Requisicao
from meuservico_pb2_grpc import MeuservicoStub
from datetime import datetime

def test_primo():
    channel = grpc.insecure_channel("localhost:50051")
    client = MeuservicoStub(channel)
    resp1 = client.ehPrimo(Requisicao(id=1))
    i = resp1.texto.find("1 eh primo")
    assert i != -1

def test_naoprimo():
    channel = grpc.insecure_channel("localhost:50051")
    client = MeuservicoStub(channel)

    resp1 = client.ehPrimo(Requisicao(id=4))
    i = resp1.texto.find("4 NAO eh primo")
    assert i != -1

#test_primo()
#test_naoprimo()
#print("fim")

