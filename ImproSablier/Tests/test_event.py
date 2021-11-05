import pytest
from Libs.Event.event import event,eventType,eventPriority
from Libs.Event.eventLoop import eventLoop
from Libs.Event.eventQueue import eventQueue
import itertools
    
def test_event_init():
    event.newid = itertools.count()
    firstEvent = event(eventType.TEST_EVENT, eventPriority.EVENT_PRIORITY_GAME)
    assert firstEvent.getId() == 0
    
def test_event_id_incrementation():
    event.newid = itertools.count()
    firstEvent = event(eventType.TEST_EVENT, eventPriority.EVENT_PRIORITY_GAME)
    secondEvent = event(eventType.TEST_EVENT, eventPriority.EVENT_PRIORITY_GAME)
    assert firstEvent.getId() == 0
    assert secondEvent.getId() == 1

def test_eventQueue_init():
    event.newid = itertools.count()
    eventQ = eventQueue()
    assert len(eventQ.eventList) == 0
    
def test_eventQueue_addEvents():
    event.newid = itertools.count()
    eventQ = eventQueue()
    firstEvent = event(eventType.TEST_EVENT, eventPriority.EVENT_PRIORITY_GAME)
    eventQ.addEvent(firstEvent)
    assert len(eventQ.eventList) == 1
    secondEvent = event(eventType.TEST_EVENT, eventPriority.EVENT_PRIORITY_GAME)
    eventQ.addEvent(secondEvent)
    assert len(eventQ.eventList) == 2 

def test_eventQueue_popEvents():
    event.newid = itertools.count()
    eventQ = eventQueue()
    firstEvent = event(eventType.TEST_EVENT, eventPriority.EVENT_PRIORITY_GAME)
    eventQ.addEvent(firstEvent)
    assert len(eventQ.eventList) == 1
    secondEvent = event(eventType.TEST_EVENT, eventPriority.EVENT_PRIORITY_GAME)
    eventQ.addEvent(secondEvent)
    assert len(eventQ.eventList) == 2
    eventPopped = eventQ.popFirstEvent()
    assert len(eventQ.eventList) == 1
    assert eventPopped.getId() == firstEvent.getId()
    eventPopped = eventQ.popFirstEvent()
    assert len(eventQ.eventList) == 0
    assert eventPopped.getId() == secondEvent.getId()

