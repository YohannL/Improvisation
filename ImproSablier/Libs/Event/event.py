from enum import Enum
import itertools

class eventType(Enum):
    TEST_EVENT = 0 # First Time connection
    PUBLIC_CONNECT = 1 # First Time connection
    PUBLIC_ADD_TIME = 2 # Add Time to player
    ADMIN_CHANGE_STATUS = 10 # Change status of the game
    ADMIN_ADD_TIME = 11 # Add Time to player
    ADMIN_REMOVE_TIME = 12 # Remove Time to player
    ADMIN_START_TIMER = 12 # Start Time for a player
    ADMIN_RESET = 13 # Start Time for a player
    GAME_ADD_TIME = 20 # Start Time for a player

class eventPriority(Enum):
    EVENT_PRIORITY_GAME = 0
    EVENT_PRIORITY_ADMIN = 1
    EVENT_PRIORITY_PUBLIC = 2

class event():
    newid = itertools.count()

    def __init__(self, type= eventType.TEST_EVENT , priority= eventPriority.EVENT_PRIORITY_PUBLIC):
        self.id = next(event.newid)
        self.eventType = type
        self.priority = priority

    def getId(self):
        return self.id

    def getPriority(self):
        return self.priority

    def getEventType(self):
        return self.eventType

    def getPlayer(self):
        pass


class eventPublicConnect(event):
    def __init__(self, ip):
        super().__init__(type= eventType.PUBLIC_CONNECT,priority=eventPriority.EVENT_PRIORITY_PUBLIC)
        self._ip=ip

    def getIp(self):
        return self._ip

class eventPublicAddTime(event):
    def __init__(self, ip, player):
        super().__init__(type= eventType.PUBLIC_USE_TIME,priority=eventPriority.EVENT_PRIORITY_PUBLIC)
        self._player = player 
        self._ip = ip

    def getIp(self):
        return self._ip

    def getPlayer(self):
        return self._player

class eventAdminChangeStatus(event):
    def __init__(self, status):
        super().__init__(type= eventType.ADMIN_CHANGE_STATUS,priority=eventPriority.EVENT_PRIORITY_ADMIN)
        self._status = status 

    def getStatus(self):
        return self._status

class eventAdminAddTime(event):
    def __init__(self, player):
        super().__init__(type= eventType.ADMIN_ADD_TIME,priority=eventPriority.EVENT_PRIORITY_ADMIN)
        self._player = player 

    def getPlayer(self):
        return self._player
        
class eventGameAddTime(event):
    def __init__(self, player):
        super().__init__(type= eventType.GAME_ADD_TIME,priority=eventPriority.EVENT_PRIORITY_GAME)
        self._player = player 

    def getPlayer(self):
        return self._player
        
class eventAdminRemoveTime(event):
    def __init__(self, player):
        super().__init__(type= eventType.ADMIN_REMOVE_TIME,priority=eventPriority.EVENT_PRIORITY_ADMIN)
        self._player = player 

    def getPlayer(self):
        return self._player
        
class eventAdminStartTimer(event):
    def __init__(self, player):
        super().__init__(type= eventType.ADMIN_START_TIMER,priority=eventPriority.EVENT_PRIORITY_ADMIN)
        self._player = player 

    def getPlayer(self):
        return self._player
        
class eventAdminReset(event):
    def __init__(self):
        super().__init__(type= eventType.ADMIN_RESET,priority=eventPriority.EVENT_PRIORITY_ADMIN)

class eventTest(event):
    def __init__(self):
        super().__init__(type= eventType.TEST_EVENT , priority= eventPriority.EVENT_PRIORITY_PUBLIC)




