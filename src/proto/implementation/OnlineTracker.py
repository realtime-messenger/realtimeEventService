import grpc

import proto.pyproto.main_pb2 as main_pb2
import proto.pyproto.main_pb2_grpc as main_pb2_grpc
from service.Tracker import Tracker


class OnlineTracker(main_pb2_grpc.OnlineTrackerServicer):
    def onConnect(self, request: main_pb2.ConnectRequest, context):
        Tracker.onConnect(
            user_id=request.userId,
            session_id=request.sessionId
        )
        return main_pb2.Void()

    def onDisconnect(self, request: main_pb2.DisconnectRequest, context):
        Tracker.onDisconnect(
            user_id=request.userId,
            session_id=request.sessionId
        )
        return main_pb2.Void()
