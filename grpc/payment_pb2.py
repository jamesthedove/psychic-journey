# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: payment.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='payment.proto',
  package='com.connectroutes.payment',
  syntax='proto3',
  serialized_options=b'Z\005proto',
  serialized_pb=b'\n\rpayment.proto\x12\x19\x63om.connectroutes.payment\"\xe7\x01\n\rPaymentOption\x12\x38\n\x06method\x18\x01 \x01(\x0e\x32(.com.connectroutes.payment.PaymentMethod\x12\n\n\x02id\x18\x02 \x01(\t\x12\x35\n\x08\x63\x61rdType\x18\x03 \x01(\x0e\x32#.com.connectroutes.payment.CardType\x12\x11\n\tcardLast4\x18\x04 \x01(\t\x12\x0b\n\x03\x62in\x18\x05 \x01(\t\x12\x13\n\x0b\x65xpiryMonth\x18\x06 \x01(\t\x12\x12\n\nexpiryYear\x18\x07 \x01(\t\x12\x10\n\x08lastUsed\x18\x08 \x01(\x03\"\x1a\n\x18GetPaymentOptionsRequest\"V\n\x19GetPaymentOptionsResponse\x12\x39\n\x07options\x18\x01 \x03(\x0b\x32(.com.connectroutes.payment.PaymentOption\"s\n\x0e\x41\x64\x64\x43\x61rdRequest\x12\x0e\n\x06\x63\x61rdNo\x18\x01 \x01(\t\x12\x17\n\x0f\x63\x61rdExpiryMonth\x18\x02 \x01(\t\x12\x16\n\x0e\x63\x61rdExpiryYear\x18\x03 \x01(\t\x12\x0f\n\x07\x63\x61rdCvv\x18\x04 \x01(\t\x12\x0f\n\x07\x63\x61rdPin\x18\x05 \x01(\t\"\x91\x01\n\x0f\x41\x64\x64\x43\x61rdResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\x12\x12\n\naction_url\x18\x03 \x01(\t\x12\x11\n\treference\x18\x04 \x01(\t\x12\x36\n\x04\x63\x61rd\x18\x05 \x01(\x0b\x32(.com.connectroutes.payment.PaymentOption\"R\n\x1eSubmitCardAuthorizationRequest\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x11\n\treference\x18\x03 \x01(\t\".\n\x19\x41\x64\x64\x43\x61rdByReferenceRequest\x12\x11\n\treference\x18\x01 \x01(\t*#\n\rPaymentMethod\x12\x08\n\x04\x63\x61sh\x10\x00\x12\x08\n\x04\x63\x61rd\x10\x01*$\n\x08\x43\x61rdType\x12\x08\n\x04visa\x10\x00\x12\x0e\n\nmastercard\x10\x01\x32\xf6\x03\n\x0ePaymentService\x12\x80\x01\n\x11GetPaymentOptions\x12\x33.com.connectroutes.payment.GetPaymentOptionsRequest\x1a\x34.com.connectroutes.payment.GetPaymentOptionsResponse\"\x00\x12\x62\n\x07\x41\x64\x64\x43\x61rd\x12).com.connectroutes.payment.AddCardRequest\x1a*.com.connectroutes.payment.AddCardResponse\"\x00\x12\x82\x01\n\x17SubmitCardAuthorization\x12\x39.com.connectroutes.payment.SubmitCardAuthorizationRequest\x1a*.com.connectroutes.payment.AddCardResponse\"\x00\x12x\n\x12\x41\x64\x64\x43\x61rdByReference\x12\x34.com.connectroutes.payment.AddCardByReferenceRequest\x1a*.com.connectroutes.payment.AddCardResponse\"\x00\x42\x07Z\x05protob\x06proto3'
)

_PAYMENTMETHOD = _descriptor.EnumDescriptor(
  name='PaymentMethod',
  full_name='com.connectroutes.payment.PaymentMethod',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='cash', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='card', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=791,
  serialized_end=826,
)
_sym_db.RegisterEnumDescriptor(_PAYMENTMETHOD)

PaymentMethod = enum_type_wrapper.EnumTypeWrapper(_PAYMENTMETHOD)
_CARDTYPE = _descriptor.EnumDescriptor(
  name='CardType',
  full_name='com.connectroutes.payment.CardType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='visa', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='mastercard', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=828,
  serialized_end=864,
)
_sym_db.RegisterEnumDescriptor(_CARDTYPE)

CardType = enum_type_wrapper.EnumTypeWrapper(_CARDTYPE)
cash = 0
card = 1
visa = 0
mastercard = 1



_PAYMENTOPTION = _descriptor.Descriptor(
  name='PaymentOption',
  full_name='com.connectroutes.payment.PaymentOption',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='method', full_name='com.connectroutes.payment.PaymentOption.method', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='com.connectroutes.payment.PaymentOption.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cardType', full_name='com.connectroutes.payment.PaymentOption.cardType', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cardLast4', full_name='com.connectroutes.payment.PaymentOption.cardLast4', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bin', full_name='com.connectroutes.payment.PaymentOption.bin', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiryMonth', full_name='com.connectroutes.payment.PaymentOption.expiryMonth', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiryYear', full_name='com.connectroutes.payment.PaymentOption.expiryYear', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastUsed', full_name='com.connectroutes.payment.PaymentOption.lastUsed', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=45,
  serialized_end=276,
)


_GETPAYMENTOPTIONSREQUEST = _descriptor.Descriptor(
  name='GetPaymentOptionsRequest',
  full_name='com.connectroutes.payment.GetPaymentOptionsRequest',
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
  serialized_start=278,
  serialized_end=304,
)


_GETPAYMENTOPTIONSRESPONSE = _descriptor.Descriptor(
  name='GetPaymentOptionsResponse',
  full_name='com.connectroutes.payment.GetPaymentOptionsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='options', full_name='com.connectroutes.payment.GetPaymentOptionsResponse.options', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=306,
  serialized_end=392,
)


_ADDCARDREQUEST = _descriptor.Descriptor(
  name='AddCardRequest',
  full_name='com.connectroutes.payment.AddCardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cardNo', full_name='com.connectroutes.payment.AddCardRequest.cardNo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cardExpiryMonth', full_name='com.connectroutes.payment.AddCardRequest.cardExpiryMonth', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cardExpiryYear', full_name='com.connectroutes.payment.AddCardRequest.cardExpiryYear', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cardCvv', full_name='com.connectroutes.payment.AddCardRequest.cardCvv', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cardPin', full_name='com.connectroutes.payment.AddCardRequest.cardPin', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=394,
  serialized_end=509,
)


_ADDCARDRESPONSE = _descriptor.Descriptor(
  name='AddCardResponse',
  full_name='com.connectroutes.payment.AddCardResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='com.connectroutes.payment.AddCardResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action', full_name='com.connectroutes.payment.AddCardResponse.action', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='action_url', full_name='com.connectroutes.payment.AddCardResponse.action_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reference', full_name='com.connectroutes.payment.AddCardResponse.reference', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='card', full_name='com.connectroutes.payment.AddCardResponse.card', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=512,
  serialized_end=657,
)


_SUBMITCARDAUTHORIZATIONREQUEST = _descriptor.Descriptor(
  name='SubmitCardAuthorizationRequest',
  full_name='com.connectroutes.payment.SubmitCardAuthorizationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='com.connectroutes.payment.SubmitCardAuthorizationRequest.action', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='com.connectroutes.payment.SubmitCardAuthorizationRequest.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reference', full_name='com.connectroutes.payment.SubmitCardAuthorizationRequest.reference', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=659,
  serialized_end=741,
)


_ADDCARDBYREFERENCEREQUEST = _descriptor.Descriptor(
  name='AddCardByReferenceRequest',
  full_name='com.connectroutes.payment.AddCardByReferenceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference', full_name='com.connectroutes.payment.AddCardByReferenceRequest.reference', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=743,
  serialized_end=789,
)

_PAYMENTOPTION.fields_by_name['method'].enum_type = _PAYMENTMETHOD
_PAYMENTOPTION.fields_by_name['cardType'].enum_type = _CARDTYPE
_GETPAYMENTOPTIONSRESPONSE.fields_by_name['options'].message_type = _PAYMENTOPTION
_ADDCARDRESPONSE.fields_by_name['card'].message_type = _PAYMENTOPTION
DESCRIPTOR.message_types_by_name['PaymentOption'] = _PAYMENTOPTION
DESCRIPTOR.message_types_by_name['GetPaymentOptionsRequest'] = _GETPAYMENTOPTIONSREQUEST
DESCRIPTOR.message_types_by_name['GetPaymentOptionsResponse'] = _GETPAYMENTOPTIONSRESPONSE
DESCRIPTOR.message_types_by_name['AddCardRequest'] = _ADDCARDREQUEST
DESCRIPTOR.message_types_by_name['AddCardResponse'] = _ADDCARDRESPONSE
DESCRIPTOR.message_types_by_name['SubmitCardAuthorizationRequest'] = _SUBMITCARDAUTHORIZATIONREQUEST
DESCRIPTOR.message_types_by_name['AddCardByReferenceRequest'] = _ADDCARDBYREFERENCEREQUEST
DESCRIPTOR.enum_types_by_name['PaymentMethod'] = _PAYMENTMETHOD
DESCRIPTOR.enum_types_by_name['CardType'] = _CARDTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PaymentOption = _reflection.GeneratedProtocolMessageType('PaymentOption', (_message.Message,), {
  'DESCRIPTOR' : _PAYMENTOPTION,
  '__module__' : 'payment_pb2'
  # @@protoc_insertion_point(class_scope:com.connectroutes.payment.PaymentOption)
  })
_sym_db.RegisterMessage(PaymentOption)

GetPaymentOptionsRequest = _reflection.GeneratedProtocolMessageType('GetPaymentOptionsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPAYMENTOPTIONSREQUEST,
  '__module__' : 'payment_pb2'
  # @@protoc_insertion_point(class_scope:com.connectroutes.payment.GetPaymentOptionsRequest)
  })
_sym_db.RegisterMessage(GetPaymentOptionsRequest)

GetPaymentOptionsResponse = _reflection.GeneratedProtocolMessageType('GetPaymentOptionsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPAYMENTOPTIONSRESPONSE,
  '__module__' : 'payment_pb2'
  # @@protoc_insertion_point(class_scope:com.connectroutes.payment.GetPaymentOptionsResponse)
  })
_sym_db.RegisterMessage(GetPaymentOptionsResponse)

AddCardRequest = _reflection.GeneratedProtocolMessageType('AddCardRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDCARDREQUEST,
  '__module__' : 'payment_pb2'
  # @@protoc_insertion_point(class_scope:com.connectroutes.payment.AddCardRequest)
  })
_sym_db.RegisterMessage(AddCardRequest)

AddCardResponse = _reflection.GeneratedProtocolMessageType('AddCardResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDCARDRESPONSE,
  '__module__' : 'payment_pb2'
  # @@protoc_insertion_point(class_scope:com.connectroutes.payment.AddCardResponse)
  })
_sym_db.RegisterMessage(AddCardResponse)

SubmitCardAuthorizationRequest = _reflection.GeneratedProtocolMessageType('SubmitCardAuthorizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBMITCARDAUTHORIZATIONREQUEST,
  '__module__' : 'payment_pb2'
  # @@protoc_insertion_point(class_scope:com.connectroutes.payment.SubmitCardAuthorizationRequest)
  })
_sym_db.RegisterMessage(SubmitCardAuthorizationRequest)

AddCardByReferenceRequest = _reflection.GeneratedProtocolMessageType('AddCardByReferenceRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDCARDBYREFERENCEREQUEST,
  '__module__' : 'payment_pb2'
  # @@protoc_insertion_point(class_scope:com.connectroutes.payment.AddCardByReferenceRequest)
  })
_sym_db.RegisterMessage(AddCardByReferenceRequest)


DESCRIPTOR._options = None

_PAYMENTSERVICE = _descriptor.ServiceDescriptor(
  name='PaymentService',
  full_name='com.connectroutes.payment.PaymentService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=867,
  serialized_end=1369,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetPaymentOptions',
    full_name='com.connectroutes.payment.PaymentService.GetPaymentOptions',
    index=0,
    containing_service=None,
    input_type=_GETPAYMENTOPTIONSREQUEST,
    output_type=_GETPAYMENTOPTIONSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddCard',
    full_name='com.connectroutes.payment.PaymentService.AddCard',
    index=1,
    containing_service=None,
    input_type=_ADDCARDREQUEST,
    output_type=_ADDCARDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SubmitCardAuthorization',
    full_name='com.connectroutes.payment.PaymentService.SubmitCardAuthorization',
    index=2,
    containing_service=None,
    input_type=_SUBMITCARDAUTHORIZATIONREQUEST,
    output_type=_ADDCARDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddCardByReference',
    full_name='com.connectroutes.payment.PaymentService.AddCardByReference',
    index=3,
    containing_service=None,
    input_type=_ADDCARDBYREFERENCEREQUEST,
    output_type=_ADDCARDRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PAYMENTSERVICE)

DESCRIPTOR.services_by_name['PaymentService'] = _PAYMENTSERVICE

# @@protoc_insertion_point(module_scope)
