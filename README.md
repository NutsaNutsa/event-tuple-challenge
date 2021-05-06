# event-tuple

Helper classes for Event tuples

## Install


Inside of a new virtualenv, you can pip install this module by doing the following :

```
$ .env) pip install git+https://github.com/NutsaNutsa/event-tuple-challenge.git@main
```


## How to test

We make use of `pytest` which can be launched as follows:

```
$ .env) pytest -s
```

## Challenge 5


The solution that comes to mind:

I would have a dictionary of "event factories" with EventTuple as a resolver function,
EventTuple takes in two arguments:
    first is the name of the class it wants to initialize
    second is the list of the tuples
EventTuple should also have a way to connect the first argument to the correct __init__ function:
this can simply be done by having a dictionary i.e:
```
    res = {
        "UserClickedOnButton": UserClickedOnButtonEvent,
        "UserLongPressed": UserLongPressedEvent
    }
```
(this is probably the easiest solution to implement (however not the only one))

EventTuple should look up the class by the name and run __init__ for it
as we do not know the order of which the arguments will be sorted in the second argument of the EventTuple
we should also convert second argument to kwargs dictionary and pass it using **kwargs

so the function should look something like this:
```
    res = {
        "UserClickedOnButton": UserClickedOnButtonEvent,
        "UserLongPressed": UserLongPressedEvent
    }
    kwargs = {}
    for arg in arg_list:
        kwargs[arg[0]] = arg[1]
    return res[event_type](**kwargs)
```

Additionally i would also have UserClickedOnButtonEvent, UserLongPressedEvent and all other events extend the same class that will take care of providing and initializing fields needed in "event" classes i.e:
```
    def timestamp(self):
        return self._event_id.timestamp().int
    
    def event_id(self):
        return self._event_id
    
    def event_type(self):
        return self._event_type
```

I did also provide a sample implementation in the [event_tuple.py](https://github.com/NutsaNutsa/event-tuple-challenge/blob/challenge-5/pokerdevs/event_tuple/event_tuple.py).
**Thank you**