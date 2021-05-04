import pytest
import logging
from pokerdevs import event_tuple


logger = logging.getLogger(__name__)


def generate_test_events():
    yield ("b5796505-68fd-40d5-814a-9d31f3f084b0", 1619146052, "UserClickedOnButton", "close_button")
    yield ("1d0bfda2-fe1d-4c61-a8bb-2c7df89beddf", 1619146123, "UserLongPressed", 340, 420)

def serialize_event(event):
    return f"Event '{event[2]}' occurred at {event[1]} with ID: {event[0]}"



def test_event_tuple():
    logger.info(f"Starting the test !")    
    for event in generate_test_events():
        print(serialize_event(event))