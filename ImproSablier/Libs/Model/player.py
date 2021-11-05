import json

class Player():

    def __init__(self, color : str, time: int, timeMax : int):
        self.color = color
        self.time = time
        self.timeMax = timeMax
        self.isPlaying = False

    def get_time(self):
        return self.time
    
    def set_time(self, time: int):
        self.time = time

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

    def set_timeMax(self, timeMax):
        self.timeMax = timeMax

    def isTimeAddable(self):
        if (self.timeMax == 0 ):
            return True # We are in demo Mode, so no limit to add time
        elif (self.time < self.timeMax):
            return True # Player time is not at the max
        else:
            return False # Player is at the max

    def reset(self, timeMax):
        self.time = timeMax
        self.timeMax = timeMax

    def addTime(self, timeToAdd):
        if((self.time + timeToAdd)>=0 and
         (self.time + timeToAdd)<=self.timeMax):
            self.time += timeToAdd
    
    def get_isPlaying(self):
        return self.isPlaying

    def set_isPlaying(self, isPlaying):
        self.isPlaying = isPlaying

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
        sort_keys=True, indent=4)

