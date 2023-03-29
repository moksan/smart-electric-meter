import sys
import time
from serial_processing import*
from utilities import*
from threading import Thread
from definition import*

def tryToConnectToDevice(baud):
     connected = openConnection(baud)
     if connected == True:
         setState(MessagingStates.REQ_IDENTIFICATION)
     else:
         setState(MessagingStates.FAULT_STATE)

def messagingFinalized():
     setState(MessagingStates.IDLE)
     closeConnection()

def faultState():
    closeConnection()
    setState(MessagingStates.IDLE)

def getMessageClass(messageType):
    messageClass = None

    if messageType == MessageTypes.mes_1:
        messageClass= InitilizationData()

    elif messageType == MessageTypes.mes_2:
        messageClass= InitilizationData()
        
    return messageClass

def commonSendMessage(messageType, obis_code ,nextMessageState, _callback = None):
    messageClass = getMessageClass(messageType)
    #If it needs to change, use callback function
    if _callback:
        messageClass = _callback(messageClass)
    writePort(obis_code)
    setState(nextMessageState)

def commonGetResponseMessage_a(nextMessageState):

      respBuf = readPort_a()
     
      if respBuf != None:
              setState(nextMessageState)      
              print(respBuf)  
      else:
          setState(MessagingStates.FAULT_STATE)

      return [respBuf]

def commonGetResponseMessage_b(nextMessageState):

      respBuf = readPort_b()
     
      if respBuf != None:
              setState(nextMessageState)      
              print(respBuf)  
      else:
          setState(MessagingStates.FAULT_STATE)

      return [respBuf]     