# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import profile_pb2 as profile__pb2


class ProfileServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadDocument = channel.stream_unary(
                '/com.connectroutes.profile.ProfileService/UploadDocument',
                request_serializer=profile__pb2.Chunk.SerializeToString,
                response_deserializer=profile__pb2.UploadDocumentResponse.FromString,
                )
        self.UpdateProfile = channel.unary_unary(
                '/com.connectroutes.profile.ProfileService/UpdateProfile',
                request_serializer=profile__pb2.UpdateProfileRequest.SerializeToString,
                response_deserializer=profile__pb2.UpdateProfileResponse.FromString,
                )


class ProfileServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def UploadDocument(self, request_iterator, context):
        """To call the UploadDocument rpc, you need to send one of the {DocumentType} above as the first stream and the contents of the image(in chunks) in subsequent steams
        when calling UploadDocument rpc, you must pass a x-session-id meta-data representing the current user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProfile(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProfileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadDocument': grpc.stream_unary_rpc_method_handler(
                    servicer.UploadDocument,
                    request_deserializer=profile__pb2.Chunk.FromString,
                    response_serializer=profile__pb2.UploadDocumentResponse.SerializeToString,
            ),
            'UpdateProfile': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProfile,
                    request_deserializer=profile__pb2.UpdateProfileRequest.FromString,
                    response_serializer=profile__pb2.UpdateProfileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.connectroutes.profile.ProfileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProfileService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def UploadDocument(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/com.connectroutes.profile.ProfileService/UploadDocument',
            profile__pb2.Chunk.SerializeToString,
            profile__pb2.UploadDocumentResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.connectroutes.profile.ProfileService/UpdateProfile',
            profile__pb2.UpdateProfileRequest.SerializeToString,
            profile__pb2.UpdateProfileResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
