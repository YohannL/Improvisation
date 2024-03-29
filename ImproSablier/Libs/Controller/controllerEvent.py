from Libs.Event.eventLoop import eventLoop
from Libs.Event.timerLoop import timerLoop
from Libs.Event.event import *
from Libs.Model.enumeration import statusType

class ControllerEvent():
    _instance = None
    _public_nb = 0
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ControllerEvent, cls).__new__(cls)
            timerLoop()
            eventLoop()
            cls._status = statusType.STATUS_PAUSE
            eventLoop().run()
            timerLoop().run()
            # Put any initialization here.
        return cls._instance

    def admin_addTime(self,player):
        self._add_event(eventAdminAddTime(player))

    def admin_removeTime(self,player):
        self._add_event(eventAdminRemoveTime(player))

    def admin_changeStatusPlayer(self,player, isPlaying):
        self._add_event(eventAdminStartTimer(player, isPlaying))

    def admin_reset(self):
        self._add_event(eventAdminReset())
        
    def admin_fullreset(self):
        self._add_event(eventAdminFullReset())

    def public_useTime(self,id,player):
        self._add_event(eventPublicAddTime(id,player))

    def public_create(self,ip):
        if(self._status != statusType.STATUS_RUN):
            self._public_nb+=1
            self._add_event(eventPublicConnect( self._public_nb))
            return self._public_nb
        else:
            return -1

    def admin_changeStatus(self, status):
        #Update controller model        
        self._status = status
        if(self._status == statusType.STATUS_PAUSE):
            timerLoop().pause()
            #eventLoop().pause()
        elif(self._status == statusType.STATUS_RUN):
            if(not timerLoop().isRunning()):
                timerLoop().run()
            if(not eventLoop().isRunning()):
                eventLoop().run()
        elif(self._status == statusType.STATUS_RESET):
            timerLoop().pause()
            eventLoop().pause()
            # CALL RESET
        else:
            timerLoop().stop()
            eventLoop().stop()
            

    def _add_event(self, event):
        eventLoop().addEvent(event)




