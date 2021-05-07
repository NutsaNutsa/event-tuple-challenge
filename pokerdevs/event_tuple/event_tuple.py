import ulid


class EventTuple:
    def __init__(self, event_type, arg_list):
        self._event_id = ulid.new()
        self._event_type = event_type

        for arg in arg_list:
            self.add_mutable_method(arg[0], arg[1])

    def timestamp(self):
        return self._event_id.timestamp().int
    
    def event_id(self):
        return self._event_id
    
    def event_type(self):
        return self._event_type        

    def add_immutable_method(self, name, value):
        def getter():
            return value

        getter.__name__ = name
        setattr(self, getter.__name__, getter)

    def add_mutable_method(self, name, value):
        def getter():
            return getattr(self, "_" + name)

        getter.__name__ = name
        setattr(self, "_" + name, value)
        setattr(self, getter.__name__, getter)