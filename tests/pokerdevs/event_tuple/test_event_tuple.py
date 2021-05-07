import pytest
import logging
from pokerdevs.event_tuple import EventTuple


logger = logging.getLogger(__name__)


def generate_test_events():
    yield EventTuple("UserClickedOnButton", [('button_id', 'close_button'), ])
    yield EventTuple("UserLongPressed", [('x', 340), ('y', 420)])

def serialize_event(event):
	return f"Event '{event.event_type()}' occurred at {event.timestamp()} with ID: {event.event_id()}"



def test_event_tuple(): 
    logger.info(f"Starting the test !")
    for event in generate_test_events():
        print(serialize_event(event))
        print(event.get_attributes())
        for attr in event.get_attributes():
            print(attr, ": ", event.get_value(attr))