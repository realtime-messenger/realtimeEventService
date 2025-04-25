import threading
import time

from messaging.StompSender import stomp_sender
from settings import settings


class Tracker:
    instance = None
    lock = threading.Lock()

    clients_map: dict[int, set[str]] = {}

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Tracker, cls).__new__(cls)
        return cls.instance

    @classmethod
    def onConnect(cls, user_id: int, session_id: str):
        with cls.lock:
            if cls.clients_map.get(user_id) is None:
                cls.clients_map[user_id] = set()
                stomp_sender.send_online_message(user_id)

            cls.clients_map[user_id].add(session_id)
        print(cls.clients_map)

    @classmethod
    def onDisconnect(cls, user_id: int, session_id: str):
        with cls.lock:
            if cls.clients_map.get(user_id) is None:
                return

            cls.clients_map[user_id].remove(session_id)

            if len(cls.clients_map[user_id]) == 0:
                cls.clients_map.pop(user_id)
                stomp_sender.send_offline_message(user_id)
        print(cls.clients_map)

    @classmethod
    def resendOnlineUsers(cls):
        for userId in cls.clients_map:
            stomp_sender.send_online_message(userId)

    @classmethod
    def notify(cls):
        while True:
            time.sleep(
                settings.RESEND_EVENT_INTERVAL_SECONDS
            )
            cls.resendOnlineUsers()

