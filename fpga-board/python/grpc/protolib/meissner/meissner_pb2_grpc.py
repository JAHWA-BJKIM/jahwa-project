# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import protolib.meissner.meissner_pb2 as meissner__pb2


class MeissnerStub(object):
    """/////////////////////////////////////////////////
    Define RPC Service              //         
    /////////////////////////////////////////////////
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReadI2C = channel.unary_unary(
                '/meissner.Meissner/ReadI2C',
                request_serializer=meissner__pb2.ReadI2CPacket.SerializeToString,
                response_deserializer=meissner__pb2.ReadI2CResponse.FromString,
                )
        self.WriteI2C = channel.unary_unary(
                '/meissner.Meissner/WriteI2C',
                request_serializer=meissner__pb2.WriteI2CPacket.SerializeToString,
                response_deserializer=meissner__pb2.WriteI2CResponse.FromString,
                )
        self.ResetSensor = channel.unary_unary(
                '/meissner.Meissner/ResetSensor',
                request_serializer=meissner__pb2.ResetSensorPacket.SerializeToString,
                response_deserializer=meissner__pb2.ResetSensorResponse.FromString,
                )
        self.ReadSensorID = channel.unary_unary(
                '/meissner.Meissner/ReadSensorID',
                request_serializer=meissner__pb2.ReadSensorIDPacket.SerializeToString,
                response_deserializer=meissner__pb2.ReadSensorIDResponse.FromString,
                )
        self.ReadSensorVersion = channel.unary_unary(
                '/meissner.Meissner/ReadSensorVersion',
                request_serializer=meissner__pb2.ReadSensorVersionPacket.SerializeToString,
                response_deserializer=meissner__pb2.ReadSensorVersionResponse.FromString,
                )
        self.ReadSensorUniqueID = channel.unary_unary(
                '/meissner.Meissner/ReadSensorUniqueID',
                request_serializer=meissner__pb2.ReadSensorUniqueIDPacket.SerializeToString,
                response_deserializer=meissner__pb2.ReadSensorUniqueIDResponse.FromString,
                )
        self.TestI2CConnection = channel.unary_unary(
                '/meissner.Meissner/TestI2CConnection',
                request_serializer=meissner__pb2.TestI2CConnectionPacket.SerializeToString,
                response_deserializer=meissner__pb2.TestI2CConnectionResponse.FromString,
                )
        self.TestSensorTemperature = channel.unary_unary(
                '/meissner.Meissner/TestSensorTemperature',
                request_serializer=meissner__pb2.TestSensorTemperaturePacket.SerializeToString,
                response_deserializer=meissner__pb2.TestSensorTemperatureResponse.FromString,
                )
        self.TestSensorSupplyVoltage = channel.unary_unary(
                '/meissner.Meissner/TestSensorSupplyVoltage',
                request_serializer=meissner__pb2.TestSensorSupplyVoltagePacket.SerializeToString,
                response_deserializer=meissner__pb2.TestSensorSupplyVoltageResponse.FromString,
                )
        self.TestSensorOutputVoltage = channel.unary_unary(
                '/meissner.Meissner/TestSensorOutputVoltage',
                request_serializer=meissner__pb2.TestSensorOutputVoltagePacket.SerializeToString,
                response_deserializer=meissner__pb2.TestSensorOutputVoltageResponse.FromString,
                )
        self.TestAFESensorConnectivity = channel.unary_unary(
                '/meissner.Meissner/TestAFESensorConnectivity',
                request_serializer=meissner__pb2.TestAFESensorConnectivityPacket.SerializeToString,
                response_deserializer=meissner__pb2.TestAFESensorConnectivityResponse.FromString,
                )


class MeissnerServicer(object):
    """/////////////////////////////////////////////////
    Define RPC Service              //         
    /////////////////////////////////////////////////
    """

    def ReadI2C(self, request, context):
        """Read I2C
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteI2C(self, request, context):
        """Write I2C
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetSensor(self, request, context):
        """Reset Sensor
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadSensorID(self, request, context):
        """Read Sensor ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadSensorVersion(self, request, context):
        """Read Sensor Version
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadSensorUniqueID(self, request, context):
        """Read Sensor Unique ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestI2CConnection(self, request, context):
        """Test I2C Connection
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestSensorTemperature(self, request, context):
        """Test Sensor Temperature
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestSensorSupplyVoltage(self, request, context):
        """Test Sensor Supply Voltage
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestSensorOutputVoltage(self, request, context):
        """Test Sensor Output Voltage
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestAFESensorConnectivity(self, request, context):
        """Test AFE Sensor Connectivity
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MeissnerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReadI2C': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadI2C,
                    request_deserializer=meissner__pb2.ReadI2CPacket.FromString,
                    response_serializer=meissner__pb2.ReadI2CResponse.SerializeToString,
            ),
            'WriteI2C': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteI2C,
                    request_deserializer=meissner__pb2.WriteI2CPacket.FromString,
                    response_serializer=meissner__pb2.WriteI2CResponse.SerializeToString,
            ),
            'ResetSensor': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetSensor,
                    request_deserializer=meissner__pb2.ResetSensorPacket.FromString,
                    response_serializer=meissner__pb2.ResetSensorResponse.SerializeToString,
            ),
            'ReadSensorID': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadSensorID,
                    request_deserializer=meissner__pb2.ReadSensorIDPacket.FromString,
                    response_serializer=meissner__pb2.ReadSensorIDResponse.SerializeToString,
            ),
            'ReadSensorVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadSensorVersion,
                    request_deserializer=meissner__pb2.ReadSensorVersionPacket.FromString,
                    response_serializer=meissner__pb2.ReadSensorVersionResponse.SerializeToString,
            ),
            'ReadSensorUniqueID': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadSensorUniqueID,
                    request_deserializer=meissner__pb2.ReadSensorUniqueIDPacket.FromString,
                    response_serializer=meissner__pb2.ReadSensorUniqueIDResponse.SerializeToString,
            ),
            'TestI2CConnection': grpc.unary_unary_rpc_method_handler(
                    servicer.TestI2CConnection,
                    request_deserializer=meissner__pb2.TestI2CConnectionPacket.FromString,
                    response_serializer=meissner__pb2.TestI2CConnectionResponse.SerializeToString,
            ),
            'TestSensorTemperature': grpc.unary_unary_rpc_method_handler(
                    servicer.TestSensorTemperature,
                    request_deserializer=meissner__pb2.TestSensorTemperaturePacket.FromString,
                    response_serializer=meissner__pb2.TestSensorTemperatureResponse.SerializeToString,
            ),
            'TestSensorSupplyVoltage': grpc.unary_unary_rpc_method_handler(
                    servicer.TestSensorSupplyVoltage,
                    request_deserializer=meissner__pb2.TestSensorSupplyVoltagePacket.FromString,
                    response_serializer=meissner__pb2.TestSensorSupplyVoltageResponse.SerializeToString,
            ),
            'TestSensorOutputVoltage': grpc.unary_unary_rpc_method_handler(
                    servicer.TestSensorOutputVoltage,
                    request_deserializer=meissner__pb2.TestSensorOutputVoltagePacket.FromString,
                    response_serializer=meissner__pb2.TestSensorOutputVoltageResponse.SerializeToString,
            ),
            'TestAFESensorConnectivity': grpc.unary_unary_rpc_method_handler(
                    servicer.TestAFESensorConnectivity,
                    request_deserializer=meissner__pb2.TestAFESensorConnectivityPacket.FromString,
                    response_serializer=meissner__pb2.TestAFESensorConnectivityResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'meissner.Meissner', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Meissner(object):
    """/////////////////////////////////////////////////
    Define RPC Service              //         
    /////////////////////////////////////////////////
    """

    @staticmethod
    def ReadI2C(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meissner.Meissner/ReadI2C',
            meissner__pb2.ReadI2CPacket.SerializeToString,
            meissner__pb2.ReadI2CResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteI2C(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meissner.Meissner/WriteI2C',
            meissner__pb2.WriteI2CPacket.SerializeToString,
            meissner__pb2.WriteI2CResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetSensor(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meissner.Meissner/ResetSensor',
            meissner__pb2.ResetSensorPacket.SerializeToString,
            meissner__pb2.ResetSensorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadSensorID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meissner.Meissner/ReadSensorID',
            meissner__pb2.ReadSensorIDPacket.SerializeToString,
            meissner__pb2.ReadSensorIDResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadSensorVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meissner.Meissner/ReadSensorVersion',
            meissner__pb2.ReadSensorVersionPacket.SerializeToString,
            meissner__pb2.ReadSensorVersionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadSensorUniqueID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meissner.Meissner/ReadSensorUniqueID',
            meissner__pb2.ReadSensorUniqueIDPacket.SerializeToString,
            meissner__pb2.ReadSensorUniqueIDResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TestI2CConnection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meissner.Meissner/TestI2CConnection',
            meissner__pb2.TestI2CConnectionPacket.SerializeToString,
            meissner__pb2.TestI2CConnectionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TestSensorTemperature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meissner.Meissner/TestSensorTemperature',
            meissner__pb2.TestSensorTemperaturePacket.SerializeToString,
            meissner__pb2.TestSensorTemperatureResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TestSensorSupplyVoltage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meissner.Meissner/TestSensorSupplyVoltage',
            meissner__pb2.TestSensorSupplyVoltagePacket.SerializeToString,
            meissner__pb2.TestSensorSupplyVoltageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TestSensorOutputVoltage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meissner.Meissner/TestSensorOutputVoltage',
            meissner__pb2.TestSensorOutputVoltagePacket.SerializeToString,
            meissner__pb2.TestSensorOutputVoltageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TestAFESensorConnectivity(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/meissner.Meissner/TestAFESensorConnectivity',
            meissner__pb2.TestAFESensorConnectivityPacket.SerializeToString,
            meissner__pb2.TestAFESensorConnectivityResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
