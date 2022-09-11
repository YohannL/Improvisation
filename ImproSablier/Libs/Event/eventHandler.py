import types
from typing import Type
from Libs.Controller.controllerModel import ControllerModel
from .event import event,eventType

class eventHandler():

    def handle(self, eventToHandle: event ):
        print("Id of event in the loop : "+str(eventToHandle.getId()) + "; Priotiry : " + str(eventToHandle.getPriority() ) )
        print("Type(object) " + str(type(eventToHandle)))
        print("getEventType " + str(eventToHandle.getEventType()))
        handleFunction = self._handle_switchFunctionHandler(eventToHandle)
        if handleFunction is not None:
            handleFunction(eventToHandle)

    def _handle_switchFunctionHandler(self, eventToHandle: event):

        switcher={
            eventType.TEST_EVENT:self._handle_testEvent,
            eventType.PUBLIC_CONNECT:self._handle_publicConnect,
            eventType.PUBLIC_ADD_TIME:self._handle_publicUseTime,
            eventType.ADMIN_CHANGE_STATUS:self._handle_adminChangeStatus,
            eventType.ADMIN_ADD_TIME:self._handle_adminAddTime,
            eventType.ADMIN_TIMER_PLAY_STATUS:self._handle_adminChangeStatusPlayer,
            eventType.ADMIN_RESET:self._handle_adminReset,
            eventType.ADMIN_REMOVE_TIME:self._handle_adminRemoveTime,
            eventType.GAME_ADD_TIME:self._handle_adminAddTime
        }
        return switcher.get(eventToHandle.getEventType(), self._handle_errorEvent)

    def _handle_publicConnect(self,eventToHandle: event):
        print("_handle_publicConnect")
        ControllerModel().public_create(eventToHandle.getIp())

    def _handle_publicUseTime(self,eventToHandle: event):
        print("_handle_publicUseTime")
        ControllerModel().public_useTime(eventToHandle.getIp(), eventToHandle.getPlayer())

    def _handle_adminChangeStatus(self,eventToHandle: event):
        print("_handle_adminChangeStatus")
        ControllerModel().admin_changeStatus(eventToHandle.getStatus())

    def _handle_adminAddTime(self,eventToHandle: event):
        print("_handle_adminAddTime")
        ControllerModel().admin_addTime(eventToHandle.getPlayer())

    def _handle_adminRemoveTime(self,eventToHandle: event):
        print("_handle_adminRemoveTime")
        ControllerModel().admin_removeTime(eventToHandle.getPlayer())

    def _handle_adminChangeStatusPlayer(self,eventToHandle: event):
        print("admin_changeStatusPlayer")
        ControllerModel().admin_changeStatusPlayer(eventToHandle.getPlayer(), eventToHandle.getIsPlaying())


    def _handle_adminReset(self,eventToHandle: event):
        print("_handle_adminReset")
        ControllerModel().admin_reset()

    def _handle_errorEvent(self,eventToHandle: event):
        print("_handle_errorEvent")
        raise("_handle_errorEvent")

    def _handle_testEvent(self,eventToHandle: event):
        print("_handle_testEvent")
