import stomp
import json

from event.UserOfflineEvent import UserOfflineEvent
from event.UserOnlineEvent import UserOnlineEvent
from settings import settings


class StompSender:
    def __init__(
            self,
            host,
            port
    ):
        self.conn = stomp.Connection([(host, port)])

    def send_online_message(self, user_id):
        try:
            event = UserOnlineEvent(userId=user_id)
            message = event.model_dump_json()
            print(message)
            self.conn.send(
                body=message,
                destination='/topic/user-online' + str(user_id))
        except Exception as e:
            print(e)

    def send_offline_message(self, user_id):
        try:
            event = UserOfflineEvent(userId=user_id)
            message = event.model_dump_json()
            print(message)
            self.conn.send(
                body=message,
                destination='/topic/user-online' + str(user_id))
        except Exception as e:
            print(e)


stomp_sender = StompSender(
    settings.RABBITMQ_HOST,
    settings.STOMP_PORT,
)