# servidorweb/servidorweb.py
import os

from flask import Flask, render_template
import grpc
import random

from meuservico_pb2 import Requisicao
from meuservico_pb2_grpc import MeuservicoStub

# cria a app flask
app = Flask(__name__)

# cria outro channel & stub
server_host2 = os.getenv("what do this do?22", "localhost")
channel2 = grpc.insecure_channel(
    f"{server_host2}:50052"
)
client2 = MeuservicoStub(channel2)


@app.route("/")
def render_homepage():
    # pegar uma resposa de microservico, pra jogar na tela, usando a funcao ehPrimo
    meuservico_response = client2.ehPrimo(
        Requisicao( id = random.randrange(1,50,1) )
    )
    print("meuservico_response.texto = " + str(meuservico_response.texto))

    # pegar mais uma resposta de microservico, pra jogar na tela, usando a chamada1 (soh uma chamada bem simples)
    meuservico_response2 = client2.chamada1( Requisicao( id = 1)  )

    return render_template(
        "homepage.html",
        resp=meuservico_response.texto,
        resp2=meuservico_response2.texto
    )


