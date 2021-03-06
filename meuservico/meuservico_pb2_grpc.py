# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import meuservico_pb2 as meuservico__pb2


class MeuservicoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.chamada1 = channel.unary_unary(
                '/Meuservico/chamada1',
                request_serializer=meuservico__pb2.Requisicao.SerializeToString,
                response_deserializer=meuservico__pb2.Resposta.FromString,
                )
        self.chamada2 = channel.unary_unary(
                '/Meuservico/chamada2',
                request_serializer=meuservico__pb2.Requisicao.SerializeToString,
                response_deserializer=meuservico__pb2.Resposta2.FromString,
                )
        self.ehPrimo = channel.unary_unary(
                '/Meuservico/ehPrimo',
                request_serializer=meuservico__pb2.Requisicao.SerializeToString,
                response_deserializer=meuservico__pb2.Resposta.FromString,
                )


class MeuservicoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def chamada1(self, request, context):
        """apenas uma chamada que aceita Requisicao e devolve Resposta
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def chamada2(self, request, context):
        """semelhante ao item anterior
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ehPrimo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MeuservicoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'chamada1': grpc.unary_unary_rpc_method_handler(
                    servicer.chamada1,
                    request_deserializer=meuservico__pb2.Requisicao.FromString,
                    response_serializer=meuservico__pb2.Resposta.SerializeToString,
            ),
            'chamada2': grpc.unary_unary_rpc_method_handler(
                    servicer.chamada2,
                    request_deserializer=meuservico__pb2.Requisicao.FromString,
                    response_serializer=meuservico__pb2.Resposta2.SerializeToString,
            ),
            'ehPrimo': grpc.unary_unary_rpc_method_handler(
                    servicer.ehPrimo,
                    request_deserializer=meuservico__pb2.Requisicao.FromString,
                    response_serializer=meuservico__pb2.Resposta.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Meuservico', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Meuservico(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def chamada1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Meuservico/chamada1',
            meuservico__pb2.Requisicao.SerializeToString,
            meuservico__pb2.Resposta.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def chamada2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Meuservico/chamada2',
            meuservico__pb2.Requisicao.SerializeToString,
            meuservico__pb2.Resposta2.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ehPrimo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Meuservico/ehPrimo',
            meuservico__pb2.Requisicao.SerializeToString,
            meuservico__pb2.Resposta.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
