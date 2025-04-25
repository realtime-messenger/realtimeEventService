from event.BaseEvent import BaseEvent, EventType


class UserOfflineEvent(BaseEvent):
    type: EventType = EventType.UserOffline
    userId: int
