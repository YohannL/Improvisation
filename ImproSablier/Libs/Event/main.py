
from Libs.Controller.controllerEvent import ControllerEvent
import time
from Libs.Model.enumeration import statusType
from Libs.Event.event import *

if __name__ == '__main__':
    ControllerEvent()
    i = 0
    while ( i < 100):
        i+=1
        ControllerEvent().add_event(eventTest())
    
    ControllerEvent().admin_changeStatus(statusType.STATUS_RUN)
    time.sleep(10)
    ControllerEvent().admin_changeStatus(statusType.STATUS_STOP)