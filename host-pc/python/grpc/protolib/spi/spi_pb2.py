# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spi.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tspi.proto\x12\x03spi\"2\n\x1a\x43onfigureDACChannel0Packet\x12\x14\n\x0c\x63hannel_code\x18\x01 \x01(\t\"m\n\x1c\x43onfigureDACChannel0Response\x12\x16\n\x0eoperation_name\x18\x01 \x01(\t\x12\x12\n\nstart_time\x18\x02 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x03 \x01(\t\x12\x0f\n\x07success\x18\x04 \x01(\x08\"2\n\x1a\x43onfigureDACChannel1Packet\x12\x14\n\x0c\x63hannel_code\x18\x01 \x01(\t\"m\n\x1c\x43onfigureDACChannel1Response\x12\x16\n\x0eoperation_name\x18\x01 \x01(\t\x12\x12\n\nstart_time\x18\x02 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x03 \x01(\t\x12\x0f\n\x07success\x18\x04 \x01(\x08\"2\n\x1a\x43onfigureDACChannel2Packet\x12\x14\n\x0c\x63hannel_code\x18\x01 \x01(\t\"m\n\x1c\x43onfigureDACChannel2Response\x12\x16\n\x0eoperation_name\x18\x01 \x01(\t\x12\x12\n\nstart_time\x18\x02 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x03 \x01(\t\x12\x0f\n\x07success\x18\x04 \x01(\x08\"$\n\rReadADCPacket\x12\x13\n\x0b\x61\x64\x63_channel\x18\x01 \x01(\t\"s\n\x0fReadADCResponse\x12\x16\n\x0eoperation_name\x18\x01 \x01(\t\x12\x11\n\tadc_value\x18\x02 \x01(\t\x12\x12\n\nstart_time\x18\x03 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x04 \x01(\t\x12\x0f\n\x07success\x18\x05 \x01(\x08\x32\xd6\x02\n\x03SPI\x12\\\n\x14\x43onfigureDACChannel0\x12\x1f.spi.ConfigureDACChannel0Packet\x1a!.spi.ConfigureDACChannel0Response\"\x00\x12\\\n\x14\x43onfigureDACChannel1\x12\x1f.spi.ConfigureDACChannel1Packet\x1a!.spi.ConfigureDACChannel1Response\"\x00\x12\\\n\x14\x43onfigureDACChannel2\x12\x1f.spi.ConfigureDACChannel2Packet\x1a!.spi.ConfigureDACChannel2Response\"\x00\x12\x35\n\x07ReadADC\x12\x12.spi.ReadADCPacket\x1a\x14.spi.ReadADCResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spi_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CONFIGUREDACCHANNEL0PACKET._serialized_start=18
  _CONFIGUREDACCHANNEL0PACKET._serialized_end=68
  _CONFIGUREDACCHANNEL0RESPONSE._serialized_start=70
  _CONFIGUREDACCHANNEL0RESPONSE._serialized_end=179
  _CONFIGUREDACCHANNEL1PACKET._serialized_start=181
  _CONFIGUREDACCHANNEL1PACKET._serialized_end=231
  _CONFIGUREDACCHANNEL1RESPONSE._serialized_start=233
  _CONFIGUREDACCHANNEL1RESPONSE._serialized_end=342
  _CONFIGUREDACCHANNEL2PACKET._serialized_start=344
  _CONFIGUREDACCHANNEL2PACKET._serialized_end=394
  _CONFIGUREDACCHANNEL2RESPONSE._serialized_start=396
  _CONFIGUREDACCHANNEL2RESPONSE._serialized_end=505
  _READADCPACKET._serialized_start=507
  _READADCPACKET._serialized_end=543
  _READADCRESPONSE._serialized_start=545
  _READADCRESPONSE._serialized_end=660
  _SPI._serialized_start=663
  _SPI._serialized_end=1005
# @@protoc_insertion_point(module_scope)
