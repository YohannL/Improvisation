
from Libs.Model.public import Public
import json

class PublicList():

    def __init__(self):
        self.publics = []
        self.publicTimeMax = 120 # to add 
        self.publicStdTime = 10 # to add 

    def create_Public(self, ip):
        if (self._get_Public(ip) == None):
            self.publics.append(Public(self.publicTimeMax, ip))

    def get_Publics(self):
        return self.publics

    def get_Public(self, id):
        return self._get_Public(id)

    def use_Time(self,ip , player):
        enoughtTime = False
        for p in self.publics:
            if (p.get_Ip() == ip):
                enoughtTime=p.use_Time(player, self.publicStdTime)
        return enoughtTime

    def reset(self):
        for p in self.publics:  
            p.reset()            
            
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