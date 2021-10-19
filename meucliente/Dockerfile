FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY meucliente/ /service/meucliente/
WORKDIR /service/meucliente
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/meuservico.proto

ENTRYPOINT [ "python", "meucliente.py" ]
