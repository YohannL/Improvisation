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

    def reset(self, newTime):
        for key in self._ColorTimeList:
            self._ColorTimeList[key] = newTime

    def use_Time(self, colorKey, timeToDescrease):
        if(colorKey in self._ColorTimeList):
            if(self._ColorTimeList[colorKey] >= timeToDescrease):
                self._ColorTimeList[colorKey] -= timeToDescrease
                return True
            else:
                timeAdded = self._ColorTimeList[colorKey]
                self._ColorTimeList[colorKey] = 0
                print("Public Warning : Not enought time to give")
                return False
        else:
            print("Public Error : Try to remove non existing color : " + colorKey)
            return 0

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
