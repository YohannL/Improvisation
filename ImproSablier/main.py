from Libs.Controller.controllerEvent import ControllerEvent
from Libs.Controller.controllerModel import ControllerModel
from Api.api import *
from Libs.Log.Logger import Logger
from Libs.Model.enumeration import statusType
import configparser


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    name = config['log']['main_name']
    level = config['log']['level'] 
    Logger(name=name,levelIn=level)
    
    if config['api']['apiDbg'] == "True":
        dbg = True
    else:
        dbg = False
    controller = ControllerEvent()
    controller.admin_changeStatus(statusType.STATUS_PAUSE)
    
        
    ApiApp.run(host=config['api']['apiHost'], port=config['main']['port'], debug=dbg)
