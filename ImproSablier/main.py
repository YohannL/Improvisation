from Libs.Controller.controllerEvent import ControllerEvent
from Libs.Controller.controllerModel import ControllerModel
from Api.api import *
from Libs.Model.enumeration import statusType
from Libs.Model.enumeration import playerColor

if __name__ == '__main__':
    controller = ControllerEvent()
    # controller.admin_changeStatus(statusType.STATUS_RUN_EVENT_LOOP)
    ApiApp.run(host=ApiHost, port=ApiPort, debug=ApiDbg)
