from Libs.Model.model import Model
from Libs.View.view import View

class ControllerModel():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the ControllerModel')
            cls._instance = super(ControllerModel, cls).__new__(cls)
            cls._instance.model = Model()
            cls._instance.view = View()
            cls._instance.currentIdPublic = 0
            # Put any initialization here.
        return cls._instance

    def reset(self):
        self.model.reset()

    # public functions
    def public_create(self,ip):
        self.currentIdPublic += 1
        self.model.add_Public(ip)
        return self.currentIdPublic

    def public_useTime(self,ip,player):
        return self.model.public_useTime(ip, player)

    def get_Publics(self):
        return self.model.get_publics()

    # admin functions


    def admin_addTime(self, player):
        if(self.model.get_PlayerList().get_Player(player).time < self.model.get_PlayerList().get_Player(player).timeMax):
            self.model.admin_addTime(player)
            return True
        return False

    def admin_removeTime(self, player):
        if(self.model.get_PlayerList().get_Player(player).time > 0):
            self.model.admin_removeTime(player)
            return True
        return False

    def admin_toogleTimer(self, player):
        return self.model.admin_toogleTimer(player)

    def admin_reset(self):
        print("admin_reset")

    def get_Public(self, id):
        return self.model.get_Public(id)

    def get_PlayerList(self):
        return self.model.get_PlayerList()

    def get_Player(self, color):
        return self.model.get_PlayerList().get_Player(color)



