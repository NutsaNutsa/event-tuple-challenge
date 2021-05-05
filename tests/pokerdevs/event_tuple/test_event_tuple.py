import pytest
import logging
from pokerdevs.event_tuple import UserClickedOnButtonEvent, UserLongPressedEvent


logger = logging.getLogger(__name__)


def generate_test_events():
    yield UserClickedOnButtonEvent.create(button_id='close_button')
    yield UserLongPressedEvent.create(x=340, y=420)

def serialize_event(event):
	return f"Event '{event.event_type()}' occurred at {event.timestamp()} with ID: {event.event_id()}"



def test_event_tuple():
    logger.info(f"Starting the test !")
    for event in generate_test_events():
        print(serialize_event(event))