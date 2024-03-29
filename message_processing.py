from definition import *
from sequence import *
from serial_processing import *
from utilities import *

sys.path.append("C:/Users/m.oksan/Desktop/makel/smart-electric-meter")

def startInitilizationReadoutSequence(baud):

    while 1:
        if getState() == MessagingStates.IDLE:
            setState(MessagingStates.TRY_TO_CONNECT_TO_DEVICE)

        elif getState() == MessagingStates.TRY_TO_CONNECT_TO_DEVICE:
            tryToConnectToDevice(baud)

        elif getState() == MessagingStates.FAULT_STATE:
            faultState()
            break

        elif getState() == MessagingStates.REQ_IDENTIFICATION:
            #commonSendMessage(MessageTypes.mes_1,obis_code, MessagingStates.RESP_IDENTIFICATION, None)
            identification_electric_meter()
            setState(MessagingStates.RESP_IDENTIFICATION)

        elif getState() == MessagingStates.RESP_IDENTIFICATION:
             commonGetResponseMessage_a(MessagingStates.REQ_BAUD_INITILIZATION)

        elif getState() == MessagingStates.REQ_BAUD_INITILIZATION:
              initilization_comm_baudrate(5)
              setState(MessagingStates.MESSAGING_FINALIZED)

        elif getState() == MessagingStates.MESSAGING_FINALIZED:
            messagingFinalized()
            break

def startReadoutSequence(baud):

    while 1:
        if getState() == MessagingStates.IDLE:
            setState(MessagingStates.TRY_TO_CONNECT_TO_DEVICE)

        elif getState() == MessagingStates.TRY_TO_CONNECT_TO_DEVICE:
            tryToConnectToDevice(baud)
            setState(MessagingStates.REQ_READOUT_MESSAGE)

        elif getState() == MessagingStates.FAULT_STATE:
            faultState()
            break

        elif getState() == MessagingStates.REQ_READOUT_MESSAGE:
            #commonSendMessage(MessageTypes.mes_1, MessagingStates.RESP_IDENTIFICATION, None)
            commonGetResponseMessage_b(MessagingStates.MESSAGING_FINALIZED ,24)

        elif getState() == MessagingStates.MESSAGING_FINALIZED:
            terminate_comm_code()
            messagingFinalized()
            break        

def startInitilizationProgModeSequence(baud):

    while 1:
        if getState() == MessagingStates.IDLE:
            setState(MessagingStates.TRY_TO_CONNECT_TO_DEVICE)

        elif getState() == MessagingStates.TRY_TO_CONNECT_TO_DEVICE:
            tryToConnectToDevice(baud)

        elif getState() == MessagingStates.FAULT_STATE:
            faultState()
            break

        elif getState() == MessagingStates.REQ_IDENTIFICATION:
            #commonSendMessage(MessageTypes.mes_1,obis_code, MessagingStates.RESP_IDENTIFICATION, None)
            identification_electric_meter()
            setState(MessagingStates.RESP_IDENTIFICATION)

        elif getState() == MessagingStates.RESP_IDENTIFICATION:
             commonGetResponseMessage_a(MessagingStates.REQ_BAUD_INITILIZATION)

        elif getState() == MessagingStates.REQ_BAUD_INITILIZATION:
              initilization_prog_mode(5)
              setState(MessagingStates.MESSAGING_FINALIZED)

        elif getState() == MessagingStates.MESSAGING_FINALIZED:
            messagingFinalized()
            break

def startReadObis_T_Sequence(baud):

    while 1:
        if getState() == MessagingStates.IDLE:
            setState(MessagingStates.TRY_TO_CONNECT_TO_DEVICE)

        elif getState() == MessagingStates.TRY_TO_CONNECT_TO_DEVICE:
            tryToConnectToDevice(baud)
            setState(MessagingStates.RESP_BAUD_INITILIZATION)

        elif getState() == MessagingStates.FAULT_STATE:
            faultState()
            break

        elif getState() == MessagingStates.RESP_BAUD_INITILIZATION:
            #commonSendMessage(MessageTypes.mes_1, MessagingStates.RESP_IDENTIFICATION, None)
            commonGetResponseMessage_b(MessagingStates.REQ_OBIS_MESSAGE , 16)

        elif getState() == MessagingStates.REQ_OBIS_MESSAGE:
            #commonSendMessage(MessageTypes.mes_1, MessagingStates.RESP_IDENTIFICATION, None)
            writePort_T()
            #input_param.req_param = commonGetResponseMessage_b(MessagingStates.MESSAGING_FINALIZED , 24)
            bar = commonGetResponseMessage_b(MessagingStates.MESSAGING_FINALIZED , 24)
            #commonGetResponseMessage_b(MessagingStates.MESSAGING_FINALIZED , 24)

        elif getState() == MessagingStates.MESSAGING_FINALIZED:
            terminate_comm_code()
            messagingFinalized()
            sendrequestserver(bar,'T')
            break        

def startReadObis_T1_Sequence(baud):

    while 1:
        if getState() == MessagingStates.IDLE:
            setState(MessagingStates.TRY_TO_CONNECT_TO_DEVICE)

        elif getState() == MessagingStates.TRY_TO_CONNECT_TO_DEVICE:
            tryToConnectToDevice(baud)
            setState(MessagingStates.RESP_BAUD_INITILIZATION)

        elif getState() == MessagingStates.FAULT_STATE:
            faultState()
            break

        elif getState() == MessagingStates.RESP_BAUD_INITILIZATION:
            #commonSendMessage(MessageTypes.mes_1, MessagingStates.RESP_IDENTIFICATION, None)
            commonGetResponseMessage_b(MessagingStates.REQ_OBIS_MESSAGE , 16)

        elif getState() == MessagingStates.REQ_OBIS_MESSAGE:
            #commonSendMessage(MessageTypes.mes_1, MessagingStates.RESP_IDENTIFICATION, None)
            writePort_T1()
            #input_param.req_param = commonGetResponseMessage_b(MessagingStates.MESSAGING_FINALIZED , 24)
            bar = commonGetResponseMessage_b(MessagingStates.MESSAGING_FINALIZED , 24)
            #commonGetResponseMessage_b(MessagingStates.MESSAGING_FINALIZED , 24)

        elif getState() == MessagingStates.MESSAGING_FINALIZED:
            terminate_comm_code()
            messagingFinalized()
            sendrequestserver(bar,'T1')
            break       

def startReadObis_T2_Sequence(baud):

    while 1:
        if getState() == MessagingStates.IDLE:
            setState(MessagingStates.TRY_TO_CONNECT_TO_DEVICE)

        elif getState() == MessagingStates.TRY_TO_CONNECT_TO_DEVICE:
            tryToConnectToDevice(baud)
            setState(MessagingStates.RESP_BAUD_INITILIZATION)

        elif getState() == MessagingStates.FAULT_STATE:
            faultState()
            break

        elif getState() == MessagingStates.RESP_BAUD_INITILIZATION:
            #commonSendMessage(MessageTypes.mes_1, MessagingStates.RESP_IDENTIFICATION, None)
            commonGetResponseMessage_b(MessagingStates.REQ_OBIS_MESSAGE , 16)

        elif getState() == MessagingStates.REQ_OBIS_MESSAGE:
            #commonSendMessage(MessageTypes.mes_1, MessagingStates.RESP_IDENTIFICATION, None)
            writePort_T2()
            #input_param.req_param = commonGetResponseMessage_b(MessagingStates.MESSAGING_FINALIZED , 24)
            bar = commonGetResponseMessage_b(MessagingStates.MESSAGING_FINALIZED , 24)
            #commonGetResponseMessage_b(MessagingStates.MESSAGING_FINALIZED , 24)

        elif getState() == MessagingStates.MESSAGING_FINALIZED:
            terminate_comm_code()
            messagingFinalized()
            sendrequestserver(bar,'T2')
            break                 

def startReadObis_T3_Sequence(baud):

    while 1:
        if getState() == MessagingStates.IDLE:
            setState(MessagingStates.TRY_TO_CONNECT_TO_DEVICE)

        elif getState() == MessagingStates.TRY_TO_CONNECT_TO_DEVICE:
            tryToConnectToDevice(baud)
            setState(MessagingStates.RESP_BAUD_INITILIZATION)

        elif getState() == MessagingStates.FAULT_STATE:
            faultState()
            break

        elif getState() == MessagingStates.RESP_BAUD_INITILIZATION:
            #commonSendMessage(MessageTypes.mes_1, MessagingStates.RESP_IDENTIFICATION, None)
            commonGetResponseMessage_b(MessagingStates.REQ_OBIS_MESSAGE , 16)

        elif getState() == MessagingStates.REQ_OBIS_MESSAGE:
            #commonSendMessage(MessageTypes.mes_1, MessagingStates.RESP_IDENTIFICATION, None)
            writePort_T3()
            #input_param.req_param = commonGetResponseMessage_b(MessagingStates.MESSAGING_FINALIZED , 24)
            bar = commonGetResponseMessage_b(MessagingStates.MESSAGING_FINALIZED , 24)
            #commonGetResponseMessage_b(MessagingStates.MESSAGING_FINALIZED , 24)

        elif getState() == MessagingStates.MESSAGING_FINALIZED:
            terminate_comm_code()
            messagingFinalized()
            sendrequestserver(bar,'T3')
            break        

def startReadObis_T4_Sequence(baud):

    while 1:
        if getState() == MessagingStates.IDLE:
            setState(MessagingStates.TRY_TO_CONNECT_TO_DEVICE)

        elif getState() == MessagingStates.TRY_TO_CONNECT_TO_DEVICE:
            tryToConnectToDevice(baud)
            setState(MessagingStates.RESP_BAUD_INITILIZATION)

        elif getState() == MessagingStates.FAULT_STATE:
            faultState()
            break

        elif getState() == MessagingStates.RESP_BAUD_INITILIZATION:
            #commonSendMessage(MessageTypes.mes_1, MessagingStates.RESP_IDENTIFICATION, None)
            commonGetResponseMessage_b(MessagingStates.REQ_OBIS_MESSAGE , 16)

        elif getState() == MessagingStates.REQ_OBIS_MESSAGE:
            #commonSendMessage(MessageTypes.mes_1, MessagingStates.RESP_IDENTIFICATION, None)
            writePort_T4()
            #input_param.req_param = commonGetResponseMessage_b(MessagingStates.MESSAGING_FINALIZED , 24)
            bar = commonGetResponseMessage_b(MessagingStates.MESSAGING_FINALIZED , 24)
            #commonGetResponseMessage_b(MessagingStates.MESSAGING_FINALIZED , 24)

        elif getState() == MessagingStates.MESSAGING_FINALIZED:
            terminate_comm_code()
            messagingFinalized()
            sendrequestserver(bar,'T4')
            break         