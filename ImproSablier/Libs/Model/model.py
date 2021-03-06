import sys
sys.path.append( 'Libs/Model' )
from Libs.Model.publicList import PublicList
from Libs.Model.playerList import PlayerList
from publicList import PublicList
from Libs.Model.enumeration import statusType
from Libs.Model.enumeration import playerColor

class Model():
    def __init__(self):
        print("Model : Init")
        self.playerTimeMax = 120
        self.PublicList = PublicList()
        self.PlayerList = PlayerList(self.playerTimeMax)
        self.status = statusType.STATUS_INIT
        self.playerTimeMax = 120
        self.publicTimeMax = 120

        #hardcoded init


# Accessible 
    def set_Status(self, status):
        self.status = status
        self.__update()

    def get_Status(self):
        return self.status
        
# Player :
    def set_PlayerTime(self, time):
        self.playerTimeMax = time

    def get_PlayerList(self):
        return self.PlayerList


# public 
    def add_Public(self, ip):
        self.PublicList.create_Public(ip)

    def set_PublicTime(self, time):
        self.publicTimeMax = time

    def get_PublicList(self):
        return self.PublicList.get_Publics()

    def get_Public(self, id):
        return self.PublicList.get_Public(id)

    def public_useTime(self, ip, player):
        return self.PublicList.use_Time(ip, player)

# admin 
    def admin_addTime(self, player):
        self.PlayerList.add_Time(player, 10)
        return True

    def admin_removeTime(self, player):
        self.PlayerList.add_Time(player, -10)
        return True

    def admin_toogleTimer(self, player):
        self.PlayerList.admin_toogleTimer(player)
        return True

# Not Accessible 
    def __update(self):
        for player in self.playerList:
            player.reset(self.playerTimeMax)

        for public in self.publicList:
            public.reset(self.publicTimeMax)


