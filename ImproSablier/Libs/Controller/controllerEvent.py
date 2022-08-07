from Libs.Event.eventLoop import eventLoop
from Libs.Event.timerLoop import timerLoop
from Libs.Event.event import *
from Libs.Model.enumeration import statusType

class ControllerEvent():
    _instance = None
    _public_nb = 0
    def __new__(cls):
        if cls._instance is None:
            print('Creating the ControllerEvent')
            cls._instance = super(ControllerEvent, cls).__new__(cls)
            timerLoop()
            eventLoop()
            cls._status = statusType.STATUS_RUN_EVENT_LOOP
            eventLoop().run()
            timerLoop().pause()
            # Put any initialization here.
        return cls._instance

    def admin_addTime(self,player):
        self._add_event(eventAdminAddTime(player))

    def admin_removeTime(self,player):
        self._add_event(eventAdminRemoveTime(player))

    def admin_toogleTimer(self,player):
        self._add_event(eventAdminStartTimer(player))

    def admin_reset(self):
        self._add_event(eventAdminReset())

    def public_useTime(self,id,player):
        self._add_event(eventPublicAddTime(id,player))

    def public_create(self,ip):
        self._public_nb+=1
        self._add_event(eventPublicConnect( self._public_nb))
        return self._public_nb

    def admin_changeStatus(self, status):
        #Update controller model
        if(status == statusType.STATUS_PAUSE):
            timerLoop().pause()
            eventLoop().pause()
        elif(status == statusType.STATUS_RUN_BOTH):
            if(not timerLoop().isRunning()):
                timerLoop().run()
            if(not eventLoop().isRunning()):
                eventLoop().run()
        elif(status == statusType.STATUS_RUN_EVENT_LOOP):
            if(not eventLoop().isRunning()):
                eventLoop().run()
            timerLoop().pause()
        else:
            timerLoop().stop()
            eventLoop().stop()
            
        print("admin_changeStatus")

    def _add_event(self, event):
        eventLoop().addEvent(event)




