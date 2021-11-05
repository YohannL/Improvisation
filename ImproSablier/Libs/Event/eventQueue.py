class eventQueue():
    def __init__(self):
        self.eventList = []

    def addEvent(self, event):
        self.eventList.append(event)

    def clearQueue(self):
        self.eventList.clear()
    
    def popFirstEvent(self):
        if len(self.eventList)> 0:
            return self.eventList.pop(0)
        else :
            return None
            
    def isEmpty(self):
        if len(self.eventList)> 0:
            return False
        else :
            return True