# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arguments.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='arguments.proto',
  package='recipe_engine',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x61rguments.proto\x12\rrecipe_engine\"\xa4\x07\n\tArguments\x12\x38\n\nproperties\x18\x01 \x01(\x0b\x32$.recipe_engine.Arguments.PropertyMap\x12\x42\n\x10\x61nnotation_flags\x18\x02 \x01(\x0b\x32(.recipe_engine.Arguments.AnnotationFlags\x12\x34\n\x06logdog\x18\x03 \x01(\x0b\x32$.recipe_engine.Arguments.LogDogFlags\x12:\n\x0c\x65ngine_flags\x18\x04 \x01(\x0b\x32$.recipe_engine.Arguments.EngineFlags\x1a\xd5\x01\n\x08Property\x12\x0b\n\x01s\x18\x01 \x01(\tH\x00\x12\r\n\x03int\x18\x02 \x01(\x03H\x00\x12\x0e\n\x04uint\x18\x03 \x01(\x04H\x00\x12\x0b\n\x01\x64\x18\x04 \x01(\x01H\x00\x12\x0b\n\x01\x62\x18\x05 \x01(\x08H\x00\x12\x0e\n\x04\x64\x61ta\x18\x06 \x01(\x0cH\x00\x12\x33\n\x03map\x18\x07 \x01(\x0b\x32$.recipe_engine.Arguments.PropertyMapH\x00\x12\x35\n\x04list\x18\x08 \x01(\x0b\x32%.recipe_engine.Arguments.PropertyListH\x00\x42\x07\n\x05value\x1a\x43\n\x0cPropertyList\x12\x33\n\x08property\x18\x01 \x03(\x0b\x32!.recipe_engine.Arguments.Property\x1a\xa7\x01\n\x0bPropertyMap\x12\x44\n\x08property\x18\x01 \x03(\x0b\x32\x32.recipe_engine.Arguments.PropertyMap.PropertyEntry\x1aR\n\rPropertyEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x30\n\x05value\x18\x02 \x01(\x0b\x32!.recipe_engine.Arguments.Property:\x02\x38\x01\x1aJ\n\x0f\x41nnotationFlags\x12\x16\n\x0e\x65mit_timestamp\x18\x01 \x01(\x08\x12\x1f\n\x17\x65mit_initial_properties\x18\x02 \x01(\x08\x1ak\n\x0bLogDogFlags\x12\x18\n\x10streamserver_uri\x18\x01 \x01(\t\x12\x11\n\tname_base\x18\x02 \x01(\t\x12\x0b\n\x03tee\x18\x03 \x01(\x08\x12\"\n\x1a\x66inal_annotation_dump_path\x18\x04 \x01(\t\x1a\'\n\x0b\x45ngineFlags\x12\x18\n\x10use_result_proto\x18\x01 \x01(\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ARGUMENTS_PROPERTY = _descriptor.Descriptor(
  name='Property',
  full_name='recipe_engine.Arguments.Property',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s', full_name='recipe_engine.Arguments.Property.s', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int', full_name='recipe_engine.Arguments.Property.int', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uint', full_name='recipe_engine.Arguments.Property.uint', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='d', full_name='recipe_engine.Arguments.Property.d', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b', full_name='recipe_engine.Arguments.Property.b', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='recipe_engine.Arguments.Property.data', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map', full_name='recipe_engine.Arguments.Property.map', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='list', full_name='recipe_engine.Arguments.Property.list', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='recipe_engine.Arguments.Property.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=289,
  serialized_end=502,
)

_ARGUMENTS_PROPERTYLIST = _descriptor.Descriptor(
  name='PropertyList',
  full_name='recipe_engine.Arguments.PropertyList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='property', full_name='recipe_engine.Arguments.PropertyList.property', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=504,
  serialized_end=571,
)

_ARGUMENTS_PROPERTYMAP_PROPERTYENTRY = _descriptor.Descriptor(
  name='PropertyEntry',
  full_name='recipe_engine.Arguments.PropertyMap.PropertyEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='recipe_engine.Arguments.PropertyMap.PropertyEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='recipe_engine.Arguments.PropertyMap.PropertyEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=659,
  serialized_end=741,
)

_ARGUMENTS_PROPERTYMAP = _descriptor.Descriptor(
  name='PropertyMap',
  full_name='recipe_engine.Arguments.PropertyMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='property', full_name='recipe_engine.Arguments.PropertyMap.property', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ARGUMENTS_PROPERTYMAP_PROPERTYENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=574,
  serialized_end=741,
)

_ARGUMENTS_ANNOTATIONFLAGS = _descriptor.Descriptor(
  name='AnnotationFlags',
  full_name='recipe_engine.Arguments.AnnotationFlags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='emit_timestamp', full_name='recipe_engine.Arguments.AnnotationFlags.emit_timestamp', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='emit_initial_properties', full_name='recipe_engine.Arguments.AnnotationFlags.emit_initial_properties', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=743,
  serialized_end=817,
)

_ARGUMENTS_LOGDOGFLAGS = _descriptor.Descriptor(
  name='LogDogFlags',
  full_name='recipe_engine.Arguments.LogDogFlags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='streamserver_uri', full_name='recipe_engine.Arguments.LogDogFlags.streamserver_uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name_base', full_name='recipe_engine.Arguments.LogDogFlags.name_base', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tee', full_name='recipe_engine.Arguments.LogDogFlags.tee', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='final_annotation_dump_path', full_name='recipe_engine.Arguments.LogDogFlags.final_annotation_dump_path', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=819,
  serialized_end=926,
)

_ARGUMENTS_ENGINEFLAGS = _descriptor.Descriptor(
  name='EngineFlags',
  full_name='recipe_engine.Arguments.EngineFlags',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='use_result_proto', full_name='recipe_engine.Arguments.EngineFlags.use_result_proto', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=928,
  serialized_end=967,
)

_ARGUMENTS = _descriptor.Descriptor(
  name='Arguments',
  full_name='recipe_engine.Arguments',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='properties', full_name='recipe_engine.Arguments.properties', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='annotation_flags', full_name='recipe_engine.Arguments.annotation_flags', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logdog', full_name='recipe_engine.Arguments.logdog', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='engine_flags', full_name='recipe_engine.Arguments.engine_flags', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ARGUMENTS_PROPERTY, _ARGUMENTS_PROPERTYLIST, _ARGUMENTS_PROPERTYMAP, _ARGUMENTS_ANNOTATIONFLAGS, _ARGUMENTS_LOGDOGFLAGS, _ARGUMENTS_ENGINEFLAGS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=967,
)

_ARGUMENTS_PROPERTY.fields_by_name['map'].message_type = _ARGUMENTS_PROPERTYMAP
_ARGUMENTS_PROPERTY.fields_by_name['list'].message_type = _ARGUMENTS_PROPERTYLIST
_ARGUMENTS_PROPERTY.containing_type = _ARGUMENTS
_ARGUMENTS_PROPERTY.oneofs_by_name['value'].fields.append(
  _ARGUMENTS_PROPERTY.fields_by_name['s'])
_ARGUMENTS_PROPERTY.fields_by_name['s'].containing_oneof = _ARGUMENTS_PROPERTY.oneofs_by_name['value']
_ARGUMENTS_PROPERTY.oneofs_by_name['value'].fields.append(
  _ARGUMENTS_PROPERTY.fields_by_name['int'])
_ARGUMENTS_PROPERTY.fields_by_name['int'].containing_oneof = _ARGUMENTS_PROPERTY.oneofs_by_name['value']
_ARGUMENTS_PROPERTY.oneofs_by_name['value'].fields.append(
  _ARGUMENTS_PROPERTY.fields_by_name['uint'])
_ARGUMENTS_PROPERTY.fields_by_name['uint'].containing_oneof = _ARGUMENTS_PROPERTY.oneofs_by_name['value']
_ARGUMENTS_PROPERTY.oneofs_by_name['value'].fields.append(
  _ARGUMENTS_PROPERTY.fields_by_name['d'])
_ARGUMENTS_PROPERTY.fields_by_name['d'].containing_oneof = _ARGUMENTS_PROPERTY.oneofs_by_name['value']
_ARGUMENTS_PROPERTY.oneofs_by_name['value'].fields.append(
  _ARGUMENTS_PROPERTY.fields_by_name['b'])
_ARGUMENTS_PROPERTY.fields_by_name['b'].containing_oneof = _ARGUMENTS_PROPERTY.oneofs_by_name['value']
_ARGUMENTS_PROPERTY.oneofs_by_name['value'].fields.append(
  _ARGUMENTS_PROPERTY.fields_by_name['data'])
_ARGUMENTS_PROPERTY.fields_by_name['data'].containing_oneof = _ARGUMENTS_PROPERTY.oneofs_by_name['value']
_ARGUMENTS_PROPERTY.oneofs_by_name['value'].fields.append(
  _ARGUMENTS_PROPERTY.fields_by_name['map'])
_ARGUMENTS_PROPERTY.fields_by_name['map'].containing_oneof = _ARGUMENTS_PROPERTY.oneofs_by_name['value']
_ARGUMENTS_PROPERTY.oneofs_by_name['value'].fields.append(
  _ARGUMENTS_PROPERTY.fields_by_name['list'])
_ARGUMENTS_PROPERTY.fields_by_name['list'].containing_oneof = _ARGUMENTS_PROPERTY.oneofs_by_name['value']
_ARGUMENTS_PROPERTYLIST.fields_by_name['property'].message_type = _ARGUMENTS_PROPERTY
_ARGUMENTS_PROPERTYLIST.containing_type = _ARGUMENTS
_ARGUMENTS_PROPERTYMAP_PROPERTYENTRY.fields_by_name['value'].message_type = _ARGUMENTS_PROPERTY
_ARGUMENTS_PROPERTYMAP_PROPERTYENTRY.containing_type = _ARGUMENTS_PROPERTYMAP
_ARGUMENTS_PROPERTYMAP.fields_by_name['property'].message_type = _ARGUMENTS_PROPERTYMAP_PROPERTYENTRY
_ARGUMENTS_PROPERTYMAP.containing_type = _ARGUMENTS
_ARGUMENTS_ANNOTATIONFLAGS.containing_type = _ARGUMENTS
_ARGUMENTS_LOGDOGFLAGS.containing_type = _ARGUMENTS
_ARGUMENTS_ENGINEFLAGS.containing_type = _ARGUMENTS
_ARGUMENTS.fields_by_name['properties'].message_type = _ARGUMENTS_PROPERTYMAP
_ARGUMENTS.fields_by_name['annotation_flags'].message_type = _ARGUMENTS_ANNOTATIONFLAGS
_ARGUMENTS.fields_by_name['logdog'].message_type = _ARGUMENTS_LOGDOGFLAGS
_ARGUMENTS.fields_by_name['engine_flags'].message_type = _ARGUMENTS_ENGINEFLAGS
DESCRIPTOR.message_types_by_name['Arguments'] = _ARGUMENTS

Arguments = _reflection.GeneratedProtocolMessageType('Arguments', (_message.Message,), dict(

  Property = _reflection.GeneratedProtocolMessageType('Property', (_message.Message,), dict(
    DESCRIPTOR = _ARGUMENTS_PROPERTY,
    __module__ = 'arguments_pb2'
    # @@protoc_insertion_point(class_scope:recipe_engine.Arguments.Property)
    ))
  ,

  PropertyList = _reflection.GeneratedProtocolMessageType('PropertyList', (_message.Message,), dict(
    DESCRIPTOR = _ARGUMENTS_PROPERTYLIST,
    __module__ = 'arguments_pb2'
    # @@protoc_insertion_point(class_scope:recipe_engine.Arguments.PropertyList)
    ))
  ,

  PropertyMap = _reflection.GeneratedProtocolMessageType('PropertyMap', (_message.Message,), dict(

    PropertyEntry = _reflection.GeneratedProtocolMessageType('PropertyEntry', (_message.Message,), dict(
      DESCRIPTOR = _ARGUMENTS_PROPERTYMAP_PROPERTYENTRY,
      __module__ = 'arguments_pb2'
      # @@protoc_insertion_point(class_scope:recipe_engine.Arguments.PropertyMap.PropertyEntry)
      ))
    ,
    DESCRIPTOR = _ARGUMENTS_PROPERTYMAP,
    __module__ = 'arguments_pb2'
    # @@protoc_insertion_point(class_scope:recipe_engine.Arguments.PropertyMap)
    ))
  ,

  AnnotationFlags = _reflection.GeneratedProtocolMessageType('AnnotationFlags', (_message.Message,), dict(
    DESCRIPTOR = _ARGUMENTS_ANNOTATIONFLAGS,
    __module__ = 'arguments_pb2'
    # @@protoc_insertion_point(class_scope:recipe_engine.Arguments.AnnotationFlags)
    ))
  ,

  LogDogFlags = _reflection.GeneratedProtocolMessageType('LogDogFlags', (_message.Message,), dict(
    DESCRIPTOR = _ARGUMENTS_LOGDOGFLAGS,
    __module__ = 'arguments_pb2'
    # @@protoc_insertion_point(class_scope:recipe_engine.Arguments.LogDogFlags)
    ))
  ,

  EngineFlags = _reflection.GeneratedProtocolMessageType('EngineFlags', (_message.Message,), dict(
    DESCRIPTOR = _ARGUMENTS_ENGINEFLAGS,
    __module__ = 'arguments_pb2'
    # @@protoc_insertion_point(class_scope:recipe_engine.Arguments.EngineFlags)
    ))
  ,
  DESCRIPTOR = _ARGUMENTS,
  __module__ = 'arguments_pb2'
  # @@protoc_insertion_point(class_scope:recipe_engine.Arguments)
  ))
_sym_db.RegisterMessage(Arguments)
_sym_db.RegisterMessage(Arguments.Property)
_sym_db.RegisterMessage(Arguments.PropertyList)
_sym_db.RegisterMessage(Arguments.PropertyMap)
_sym_db.RegisterMessage(Arguments.PropertyMap.PropertyEntry)
_sym_db.RegisterMessage(Arguments.AnnotationFlags)
_sym_db.RegisterMessage(Arguments.LogDogFlags)
_sym_db.RegisterMessage(Arguments.EngineFlags)


_ARGUMENTS_PROPERTYMAP_PROPERTYENTRY.has_options = True
_ARGUMENTS_PROPERTYMAP_PROPERTYENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
