from enum import Enum, auto

MESSAGE_TYPE = ["mem1", "mem2", "mem3"]

class input_param():
    req_param =[]
    BAUDRATE =[300,9600]

class MessageTypes(Enum):
    mes_1   = auto()
    mes_2   = auto()

class ObisCode(Enum):
    IDENTITY                     = auto()
    TRY_TO_CONNECT_TO_DEVICE     = auto()
    CONNECTED_DEVICE             = auto()
    FAULT_STATE                  = auto()
    REQ_WRITE_MESSAGE            = auto()
    RESP_WRITE_MESSAGE           = auto()

class MessagingStates(Enum):
    IDLE                         = auto()
    TRY_TO_CONNECT_TO_DEVICE     = auto()
    CONNECTED_DEVICE             = auto()
    FAULT_STATE                  = auto()
    REQ_IDENTIFICATION           = auto()
    RESP_IDENTIFICATION          = auto()
    REQ_BAUD_INITILIZATION       = auto()
    RESP_BAUD_INITILIZATION      = auto()    
    REQ_WRITE_MESSAGE            = auto()
    RESP_WRITE_MESSAGE           = auto()
    REQ_READOUT_MESSAGE          = auto()
    REQ_OBIS_MESSAGE             = auto()
    RESP_READOUT_MESSAGE         = auto()
    MESSAGING_FINALIZED         = auto()

class StatusTabStates(Enum):
    IDLE                         = auto()
    STATUS_OK                    = auto()

messagingState           = MessagingStates.IDLE

def setState(state):
    global messagingState
    messagingState = state

def getState():
    global messagingState
    return messagingState