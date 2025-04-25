from enum import Enum

from pydantic import BaseModel


class EventType(Enum):
    UserOnline = "UserOnline"
    UserOffline = "UserOffline"


class BaseEvent(BaseModel):
    type: EventType

