from Libs.Model.player import Player
from Libs.Model.enumeration import playerColor
import json

class PlayerList():

    def __init__(self, playerTimeMax):
        self.playerList = []
        self.playerTimeMax = playerTimeMax
        colorList=[playerColor.PLAYER_RED, 
        playerColor.PLAYER_BLUE, 
        playerColor.PLAYER_GREEN, 
        playerColor.PLAYER_YELLOW]
        for color in colorList:
            self.playerList.append(Player(color, self.playerTimeMax, self.playerTimeMax))

    def play_Player(self, color):
        self._get_Player(color).set_isPlaying(True)

    def stop_Player(self, color):
        self._get_Player(color).set_isPlaying(False)

    def add_Time(self, color, time):
        self._get_Player(color).addTime(time)

    def admin_changeStatusPlayer(self, color, isPlaying):
        self._get_Player(color).set_isPlaying(isPlaying)
    
    def get_Players(self):
        return self.playerList

    def get_Player(self, color):
        return self._get_Player(color)
    
    def reset(self):
        for p in self.playerList:
            p.reset(self.playerTimeMax)

    # Private function 
    def _get_Player(self, color):
        for p in self.playerList:
            if (p.get_color() == color):
                return p

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
        sort_keys=True, indent=4)

if __name__ == '__main__':
    playerList = PlayerList(1)
    print((playerList.toJSON()))
