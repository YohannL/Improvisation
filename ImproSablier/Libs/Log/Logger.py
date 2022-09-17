import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

class Logger():
    _instance = None
    def __new__(cls, name="", level=""):
        if(cls._instance == None and name!="" and level!= ""):
            cls._instance = super(Logger, cls).__new__(cls)
            path_=os.getcwd()
            name=name+"_"+datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+".log"
            cls.logger_ = logging.getLogger("LOG")
            level = cls._instance.convertLevel(level)
            cls.logger_.setLevel(level)
            if not os.path.exists(path_+"/Logs"):
                os.makedirs(path_+"/Logs")
            handler = RotatingFileHandler(path_+"/Logs/"+name, maxBytes=10*1024*1024,
                                  backupCount=1)
            formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s','%H:%M:%S')
            handler.setFormatter(formatter)
            cls.logger_.addHandler(handler)
        
        return cls._instance

    def convertLevel(cls, level):
        if level=="CRITICAL":
            return logging.CRITICAL            
        elif level=="ERROR":
            return logging.ERROR   
        elif level=="WARN":
            return logging.WARN   
        elif level=="INFO":
            return logging.INFO   
        elif level=="DEBUG":
            return logging.DEBUG   

    def critical(self, message):
        self.logger_.critical(message)
        
    def error(self, message):
        self.logger_.error(message)
        
    def warning(self, message):
        self.logger_.warning(message)
        
    def info(self, message):
        self.logger_.info(message)
        
    def debug(self, message):
        self.logger_.debug(message)