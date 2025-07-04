import threading
from concurrent import futures
import grpc

from proto.implementation.OnlineTracker import OnlineTracker
from service.Tracker import Tracker
from proto.pyproto import main_pb2_grpc as main_pb2_grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    main_pb2_grpc.add_OnlineTrackerServicer_to_server(OnlineTracker(), server)

    port = '[::]:' + "50051"
    print('Serving on port', port)

    server.add_insecure_port(port)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    Tracker()
    t1 = threading.Thread(target=Tracker.notify, daemon=True)
    t1.start()
    serve()