import ulid
import inspect
    
class UserEvent:
    def __init__(self):
        self._event_id = ulid.new()
        self._event_type = None

    def timestamp(self):
        return self._event_id.timestamp().int
    
    def event_id(self):
        return self._event_id
    
    def event_type(self):
        return self._event_type

class UserClickedOnButtonEvent(UserEvent):
    def __init__(self, button_id):
        super(UserClickedOnButtonEvent, self).__init__()
        self._event_type = "UserClickedOnButton"
        self._button_id = button_id

    def button_id(self): 
        return self._button_id

class UserLongPressedEvent(UserEvent):
    def __init__(self, x, y):
        super(UserLongPressedEvent, self).__init__()
        self._event_type = "UserLongPressed"
        self._y = y
        self._x = x

    def x(self): 
        return self._x
    
    def y(self):
        return self._y

def EventTuple(event_type, arg_list):
    res = {
        "UserClickedOnButton": UserClickedOnButtonEvent,
        "UserLongPressed": UserLongPressedEvent
    }
    kwargs = {}
    for arg in arg_list:
        kwargs[arg[0]] = arg[1]
    return res[event_type](**kwargs)
