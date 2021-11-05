
import time
from Libs.Model.enumeration import statusType
from abc import ABC, abstractmethod

class Looper(ABC):

    @abstractmethod
    def task(self):
        pass

    def isRunning(self):
        if (self._status == statusType.STATUS_RUN):
            return True
        else:
            return False

    def run(self): 
        self._mutex.acquire()
        self._status = statusType.STATUS_RUN
        self._mutex.release()
        self._thread.start()
    
    def pause(self):
        self._mutex.acquire()
        self._status = statusType.STATUS_PAUSE
        self._mutex.release()

    def stop(self, priority=0):
        # We shouldn't trigger this
        if (priority == 0) :
            self._mutex.acquire()
            self._status = statusType.STATUS_STOP
            self._mutex.release()
            self._thread.join()
        else:
            self._mutex.acquire()
            isEmpty = self.eventQueue.isEmpty()
            self._mutex.release()

            while (isEmpty is False):
                time.sleep(.5)
                self._mutex.acquire()
                isEmpty = self.eventQueue.isEmpty()
                self._mutex.release()

            self._mutex.acquire()
            self._status = statusType.STATUS_STOP
            self._mutex.release()
            self._thread.join()