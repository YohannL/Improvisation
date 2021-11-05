import time
import os
from ..Global import environment

class Logger :

    # Enum Level :
    #       info   : 3
    #       error  : 4
    #       debug  : 1
    #       warning: 2
    #       trace  : 0

    def __init__(self,configuration):        
        if type(configuration) is environment.GB_Environment:
            self.path=configuration.get("LOG", "logfile")
            self.level=int(configuration.get("LOG", "level"))
        else:
            raise TypeError("The given configuration is wrong")

    def info(self,file,msg):
        if self.level <=3:
            self.prepareLogMessage("INFO ", file, msg)
            
    def debug(self,file,msg):
        if self.level <=1:
            self.prepareLogMessage("DEBUG", file, msg)
        
    def warning(self,file,msg):
        if self.level <=2:
            self.prepareLogMessage("WARN ", file, msg)
        
    def error(self,file,msg):
        if self.level <=4:
            self.prepareLogMessage("ERROR", file, msg)
        
    def trace(self,file,msg):
        if self.level <=0:
            self.prepareLogMessage("TRACE", file, msg)
        
    def prepareLogMessage(self,typeLog,file,msg):
        msg_to_write="["+self.getSystemTime()+"]|"
        msg_to_write+="["+str(typeLog)+"]|"
        msg_to_write+="["+str(os.path.splitext(os.path.basename(file))[0])+"]| "
        msg_to_write+=msg
        msg_to_write+="\n"
        self.writeInFile(msg_to_write)        

    def getSystemTime(self):
        return time.localtime(time.time())

    def writeInFile(self, msg):
        try:
            data = open(self.path,"a+")
            data.write(msg)  
            data.close()
        except Exception as identifier:
            print("ERROR, Impossible to write log in file : Type of error: " \
                + ";Reason: " + str(identifier.args) \
                + ";inst: " + str(identifier))