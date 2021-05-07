import pytest
import logging
from pokerdevs.event_tuple import EventTuple


logger = logging.getLogger(__name__)


def generate_test_events():
    yield EventTuple("UserClickedOnButton", [('button_id', 'close_button'), ])
    yield EventTuple("UserLongPressed", [('x', 340), ('y', 420)])
    yield EventTuple("SelfDrivingCarCollisionSensorEvent", [('sensor_id', 'sensor_id value'), ('sensor_value', 5) ])
    yield EventTuple("CustomerPlacedOrderEvent", [('customer_id', 'customer_id value'), ('product_id', 'product_id value'), ('quantity', 1) ])


def serialize_event(event):
	return f"Event '{event.event_type()}' occurred at {event.timestamp()} with ID: {event.event_id()}"



def test_event_tuple(): 
    logger.info(f"Starting the test !")
    for event in generate_test_events():
        print(serialize_event(event))
        if event.event_type() == 'UserClickedOnButton':
            print(event.button_id())
        elif event.event_type() == 'UserLongPressed':
            print(event.x())
            print(event.y())
        elif event.event_type() == 'SelfDrivingCarCollisionSensorEvent':
            print(event.sensor_id())
            print(event.sensor_value())
        elif event.event_type() == 'CustomerPlacedOrderEvent':
            print(event.customer_id())
            print(event.product_id())
            print(event.quantity())

def test_event_types():
    for event in generate_test_events():
        assert isinstance(event, tuple)