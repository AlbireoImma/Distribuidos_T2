# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chat.proto',
  package='grpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nchat.proto\x12\x04grpc\"\x06\n\x04Nulo\"2\n\x07Mensaje\x12\x0f\n\x07mensaje\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\n\n\x02ts\x18\x03 \x01(\t2h\n\x0cServidorChat\x12,\n\rFlujoMensajes\x12\n.grpc.Nulo\x1a\r.grpc.Mensaje0\x01\x12*\n\rEnviarMensaje\x12\r.grpc.Mensaje\x1a\n.grpc.Nulob\x06proto3')
)




_NULO = _descriptor.Descriptor(
  name='Nulo',
  full_name='grpc.Nulo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=26,
)


_MENSAJE = _descriptor.Descriptor(
  name='Mensaje',
  full_name='grpc.Mensaje',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mensaje', full_name='grpc.Mensaje.mensaje', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='grpc.Mensaje.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ts', full_name='grpc.Mensaje.ts', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=28,
  serialized_end=78,
)

DESCRIPTOR.message_types_by_name['Nulo'] = _NULO
DESCRIPTOR.message_types_by_name['Mensaje'] = _MENSAJE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Nulo = _reflection.GeneratedProtocolMessageType('Nulo', (_message.Message,), {
  'DESCRIPTOR' : _NULO,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Nulo)
  })
_sym_db.RegisterMessage(Nulo)

Mensaje = _reflection.GeneratedProtocolMessageType('Mensaje', (_message.Message,), {
  'DESCRIPTOR' : _MENSAJE,
  '__module__' : 'chat_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Mensaje)
  })
_sym_db.RegisterMessage(Mensaje)



_SERVIDORCHAT = _descriptor.ServiceDescriptor(
  name='ServidorChat',
  full_name='grpc.ServidorChat',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=80,
  serialized_end=184,
  methods=[
  _descriptor.MethodDescriptor(
    name='FlujoMensajes',
    full_name='grpc.ServidorChat.FlujoMensajes',
    index=0,
    containing_service=None,
    input_type=_NULO,
    output_type=_MENSAJE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='EnviarMensaje',
    full_name='grpc.ServidorChat.EnviarMensaje',
    index=1,
    containing_service=None,
    input_type=_MENSAJE,
    output_type=_NULO,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVIDORCHAT)

DESCRIPTOR.services_by_name['ServidorChat'] = _SERVIDORCHAT

# @@protoc_insertion_point(module_scope)
