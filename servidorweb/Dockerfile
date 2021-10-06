FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY servidorweb/ /service/servidorweb/
WORKDIR /service/servidorweb
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/meuservico.proto

EXPOSE 5000
ENV FLASK_APP=servidorweb.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
