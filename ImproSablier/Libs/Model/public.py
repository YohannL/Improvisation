import json 
from Libs.Model.enumeration import playerColor
class Public:

    def __init__(self, timeInit, ip):
        self._ip = ip
        self._ColorTimeList = {}
        self._timeInit = timeInit        
        
        colorList=[playerColor.PLAYER_RED, 
        playerColor.PLAYER_BLUE, 
        playerColor.PLAYER_GREEN, 
        playerColor.PLAYER_YELLOW]

        for color in colorList:
            self._ColorTimeList[color] = timeInit

    def get_Ip(self):
        return self._ip

    def reset(self):
        for key in self._ColorTimeList:
            self._ColorTimeList[key] = self._timeInit

    def use_Time(self, colorKey, timeToDescrease):
        if(colorKey in self._ColorTimeList):
            if(self._ColorTimeList[colorKey] >= timeToDescrease):
                self._ColorTimeList[colorKey] -= timeToDescrease
                return timeToDescrease
            else:
                timeAdded = self._ColorTimeList[colorKey]
                self._ColorTimeList[colorKey] = 0
                print("Public Warning : Not enought time to give")
                return timeAdded
        else:
            print("Public Error : Try to remove non existing color : " + colorKey)
            return 0
        
    def has_Time(self, colorKey):
        if(colorKey in self._ColorTimeList):
            if(self._ColorTimeList[colorKey] >= 0):
                return True
            else:
                return False
        else:
            return 0
        
    def howMuch_Time(self, colorKey, timeRef):
        return min(timeRef, self._ColorTimeList[colorKey])
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
