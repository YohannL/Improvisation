from threading import Thread, Lock
import time
from Libs.Event.event import *
from Libs.Model.enumeration import statusType
from Libs.Event.looper import Looper
from Libs.Event.eventLoop import eventLoop
from Libs.Event.event import eventGameAddTime
from Libs.Model.enumeration import playerColor
from Libs.Controller.controllerModel import ControllerModel

class timerLoop(Looper):
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(timerLoop, cls).__new__(cls)
            cls._instance._mutex = Lock()
            cls._instance._status = statusType.STATUS_PAUSE #  two status : STOP and RUN
            cls._instance._thread = Thread(target=cls._instance.task)
            # Put any initialization here.
        return cls._instance

    def task(self):
        self._mutex.acquire()
        status = self._status
        self._mutex.release()
        colorList=[playerColor.PLAYER_RED, 
        playerColor.PLAYER_BLUE, 
        playerColor.PLAYER_GREEN, 
        playerColor.PLAYER_YELLOW]

        while(status != statusType.STATUS_STOP):
            if( status == statusType.STATUS_RUN):
                for color in colorList:
                    if(ControllerModel().get_Player(color).get_isPlaying() == True):
                        eventLoop().addEvent(eventAdminRemoveTime(color))
                time.sleep(1)
            else:
                # print("timerLoop : sleep")
                time.sleep(.1)

            self._mutex.acquire()
            status = self._status
            # print("timerLoop Status : "+str(status))
            self._mutex.release()
            
        print("timerLoop : Stop")
