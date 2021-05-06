import ulid

class UserClickedOnButtonEvent:
    @classmethod
    def create(cls, button_id):
        event = cls.__new__(cls)
        event._event_id = ulid.new()
        event._event_type = "UserClickedOnButton"
        event._button_id = button_id
        return event

    def timestamp(self):
        return self._event_id.timestamp().int
    
    def event_id(self):
        return self._event_id
    
    def event_type(self):
        return self._event_type

    def button_id(self): 
        return self._button_id

class UserLongPressedEvent:
    @classmethod
    def create(cls, x, y):
        event = cls.__new__(cls)
        event._event_id = ulid.new()
        event._event_type = "UserLongPressed"
        event._x = x
        event._y = y
        return event

    def timestamp(self):
        return self._event_id.timestamp().int
    
    def event_id(self):
        return self._event_id
    
    def event_type(self):
        return self._event_type

    def x(self): 
        return self._x
    
    def y(self):
        return self._y