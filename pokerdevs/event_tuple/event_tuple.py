import ulid

class EventTuple:
    def __init__(self, event_type, arg_list):
        self._event_id = ulid.new()
        self._event_type = event_type
        for arg in arg_list:
            setattr(self, arg[0], arg[1])

    def timestamp(self):
        return self._event_id.timestamp().int
    
    def event_id(self):
        return self._event_id
    
    def event_type(self):
        return self._event_type

    def get_attributes(self):
        return self.__dict__.keys()

    def get_value(self, attribute_name):
        return getattr(self, attribute_name)
