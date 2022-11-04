
from Libs.Model.public import Public
import json

class PublicList():

    def __init__(self):
        self.publics = []
        self.publicTimeMax = 120 # to add 
        self.publicStdTime = 10 # to add 
        self.mightyTimeMax = 3600

    def create_Public(self, ip):
        if (self._get_Public(ip) == None):
            self.publics.append(Public(int(self.mightyTimeMax / (len(self.publics)+1)), ip))
            
        for p in self.publics:
            p.set_TimeInit(int(self.mightyTimeMax / (len(self.publics))))
            p.reset()

    def get_Publics(self):
        return self.publics

    def get_Public(self, id):
        return self._get_Public(id)

    def has_Time(self,ip , player):
        enoughtTime = False
        for p in self.publics:
            if (p.get_Ip() == ip):
                enoughtTime=p.has_Time(player)
        return enoughtTime
    
    def howMuch_Time(self,ip , player):
        enoughtTime = False
        for p in self.publics:
            if (p.get_Ip() == ip):
                enoughtTime=p.howMuch_Time(player, self.publicStdTime)
        return enoughtTime
    
    def use_Time(self,ip , player):
        for p in self.publics:
            if (p.get_Ip() == ip):
                return p.use_Time(player, self.publicStdTime)

    def reset(self):
        for p in self.publics:  
            p.reset() 
            
    def fullreset(self):
        self.publics.clear()         
            
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
        sort_keys=True, indent=4)

    def _get_Public(self, ip):
        for p in self.publics:
            if (p.get_Ip() == ip):
                return p
        return None

if __name__ == '__main__':
    publicList = PublicList()
    publicList.create_Public("10.41.30.120")
    publicList.create_Public("10.41.30.121")
    publicList.create_Public("10.41.30.122")
    publicList.create_Public("10.41.30.123")
    print((publicList.toJSON()))