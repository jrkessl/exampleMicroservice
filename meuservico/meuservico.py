from concurrent import futures
import random
import grpc

from meuservico_pb2 import (
    Resposta, Resposta2
)

import meuservico_pb2_grpc

# Implementacao do microservico.

class MeuservicoService( meuservico_pb2_grpc.MeuservicoServicer ):
    def chamada1(self, request, context):
        return Resposta(texto="Esta eh a resposta. Foi passado inteiro: " + str(request.id))

    def chamada2(self, request, context):
        return Resposta2(texto="lala: mycall2", num=666)

    def ehPrimo(self, request, context):
        i = request.id
        ehPrimo = True

        if request.id < 0:
            return Resposta(texto=str(request.id) + " NAO eh primo. ")
        else:
            if request.id == 1:
                return Resposta(texto=str(request.id) + " eh primo. ")
            else:
                if request.id == 2:
                    return Resposta(texto=str(request.id) + " eh primo. ")
                else:
                    i = request.id-1
                    while i > 1:
                        if request.id%i == 0:
                            ehPrimo = False
                            break
                        i = i - 1
                    if ehPrimo:
                        return Resposta(texto=str(request.id) + " eh primo. ")
                    else:
                        return Resposta(texto=str(request.id) + " NAO eh primo. ")

# Codigo que faz o trabalho pesado.

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) # este eh o numero de threads para atender requisicoes. 10 eh um valor bom pra producao.
    meuservico_pb2_grpc.add_MeuservicoServicer_to_server(
        MeuservicoService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
