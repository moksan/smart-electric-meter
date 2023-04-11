import sys
import time
from threading import Thread

import requests

from definition import *
from serial_processing import *
from utilities import *


def sendrequestserver(value):

    bar = value[0]
    bar_b =  ''.join(chr(i) for i in bar[7:17])
    print(bar_b)
    deviceID = '1' # Should be string
    url = 'http://www.kulturatakplatform.com/api/'+ deviceID
    myobj = {'consumption': bar_b} # 250 sayisi yerine okudugun kwh degerini gir
    requests.post(url, json = myobj)


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
    #writePort(obis_code)
    setState(nextMessageState)

def commonGetResponseMessage_a(nextMessageState):

      respBuf = readPort_a()
     
      if respBuf != None:
              setState(nextMessageState)      
              print(respBuf)  
      else:
          setState(MessagingStates.FAULT_STATE)

      return [respBuf]

def commonGetResponseMessage_b(nextMessageState , size):

      respBuf = readPort_b(size)
     
      if respBuf != None:
              setState(nextMessageState)      
              print(respBuf)  
      else:
          setState(MessagingStates.FAULT_STATE)

      return [respBuf]     