# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import proto.chat_pb2 as chat__pb2


class ServidorChatStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.FlujoMensajes = channel.unary_stream(
        '/grpc.ServidorChat/FlujoMensajes',
        request_serializer=chat__pb2.Nulo.SerializeToString,
        response_deserializer=chat__pb2.Mensaje.FromString,
        )
    self.EnviarMensaje = channel.unary_unary(
        '/grpc.ServidorChat/EnviarMensaje',
        request_serializer=chat__pb2.Mensaje.SerializeToString,
        response_deserializer=chat__pb2.Nulo.FromString,
        )
    self.ObtenerLista = channel.unary_unary(
        '/grpc.ServidorChat/ObtenerLista',
        request_serializer=chat__pb2.Nulo.SerializeToString,
        response_deserializer=chat__pb2.Listado.FromString,
        )
    self.Registrar = channel.unary_unary(
        '/grpc.ServidorChat/Registrar',
        request_serializer=chat__pb2.Registro.SerializeToString,
        response_deserializer=chat__pb2.Nulo.FromString,
        )
    self.Desconectar = channel.unary_unary(
        '/grpc.ServidorChat/Desconectar',
        request_serializer=chat__pb2.Registro.SerializeToString,
        response_deserializer=chat__pb2.Nulo.FromString,
        )


class ServidorChatServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def FlujoMensajes(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EnviarMensaje(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ObtenerLista(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Registrar(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Desconectar(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ServidorChatServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'FlujoMensajes': grpc.unary_stream_rpc_method_handler(
          servicer.FlujoMensajes,
          request_deserializer=chat__pb2.Nulo.FromString,
          response_serializer=chat__pb2.Mensaje.SerializeToString,
      ),
      'EnviarMensaje': grpc.unary_unary_rpc_method_handler(
          servicer.EnviarMensaje,
          request_deserializer=chat__pb2.Mensaje.FromString,
          response_serializer=chat__pb2.Nulo.SerializeToString,
      ),
      'ObtenerLista': grpc.unary_unary_rpc_method_handler(
          servicer.ObtenerLista,
          request_deserializer=chat__pb2.Nulo.FromString,
          response_serializer=chat__pb2.Listado.SerializeToString,
      ),
      'Registrar': grpc.unary_unary_rpc_method_handler(
          servicer.Registrar,
          request_deserializer=chat__pb2.Registro.FromString,
          response_serializer=chat__pb2.Nulo.SerializeToString,
      ),
      'Desconectar': grpc.unary_unary_rpc_method_handler(
          servicer.Desconectar,
          request_deserializer=chat__pb2.Registro.FromString,
          response_serializer=chat__pb2.Nulo.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.ServidorChat', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))