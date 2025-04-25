from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConnectRequest(_message.Message):
    __slots__ = ("sessionId", "userId")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    userId: int
    def __init__(self, sessionId: _Optional[str] = ..., userId: _Optional[int] = ...) -> None: ...

class DisconnectRequest(_message.Message):
    __slots__ = ("sessionId", "userId")
    SESSIONID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    sessionId: str
    userId: int
    def __init__(self, sessionId: _Optional[str] = ..., userId: _Optional[int] = ...) -> None: ...

class Void(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
