from threading import Thread, Lock
import time
from Libs.Event.event import *
from Libs.Event.eventHandler import eventHandler
from Libs.Event.eventQueue import eventQueue
from Libs.Model.enumeration import statusType
from Libs.Event.looper import Looper

class eventLoop(Looper):
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(eventLoop, cls).__new__(cls)
            cls._instance._eventQueue = eventQueue()
            cls._instance._mutex = Lock()
            cls._instance._eventHandler = eventHandler() # this is a function
            cls._instance._status = statusType.STATUS_PAUSE #  3 status : STOP/RUN/PAUSE
            cls._instance._thread = Thread(target=cls._instance.task)
            # Put any initialization here.
        return cls._instance

    def addEvent(self, event):
        self._mutex.acquire()
        # print("eventLoop added")
        self._eventQueue.addEvent(event)
        self._mutex.release()

    def task(self):
        self._mutex.acquire()
        status = self._status
        self._mutex.release()

        while(status != statusType.STATUS_STOP):
            if( status == statusType.STATUS_RUN):
                self._mutex.acquire()
                eventToHandle = self._eventQueue.popFirstEvent()
                self._mutex.release()
                if eventToHandle is None:
                    time.sleep(.1)
                else:
                    self._eventHandler.handle(eventToHandle)
            else:
                time.sleep(.5)

            self._mutex.acquire()
            status = self._status
            self._mutex.release()
