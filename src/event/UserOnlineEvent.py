from event.BaseEvent import BaseEvent, EventType


class UserOnlineEvent(BaseEvent):
    type: EventType = EventType.UserOnline
    userId: int
