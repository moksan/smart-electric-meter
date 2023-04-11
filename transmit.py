#from binascii import hexlify
#from watchdog import wdTimer
import datetime as dt
import time

from pypreprocessor import pypreprocessor

from message_processing import *
from serial_processing import *
from utilities import input_param

pypreprocessor.parse()

#endexclude
#define PROGMODE

#ifdef READOUT
print('Readout Mode selected')
startInitilizationReadoutSequence(input_param.BAUDRATE[0])
startReadoutSequence(input_param.BAUDRATE[1])
#else
#ifdef PROGMODE
print('Program Mode selected')

# Save the current time to a variable ('t')
t = dt.datetime.now()

while True:
    delta = dt.datetime.now()-t
    if delta.seconds >= 10:
        startInitilizationProgModeSequence(input_param.BAUDRATE[0])
        startReadObis_T_Sequence(input_param.BAUDRATE[1])
        time.sleep(1)
        startReadObis_T1_Sequence(input_param.BAUDRATE[1])
        startReadObis_T2_Sequence(input_param.BAUDRATE[1])
        startReadObis_T3_Sequence(input_param.BAUDRATE[1])

        #print("1 Min")
        # Update 't' variable to new time
        t = dt.datetime.now()

#endifall

# def main():

#     #ifdef READOUT
#     print('Readout Mode selected')
#     startInitilizationReadoutSequence(input_param.BAUDRATE[0])
#     startReadoutSequence(input_param.BAUDRATE[1])
#     #else
#     #ifdef PROGMODE
#     print('Program Mode selected')
#     startInitilizationProgModeSequence(input_param.BAUDRATE[0])
#     startReadObisSequence(input_param.BAUDRATE[1])
#     #endifall

# if __name__ == "__main__":
#     main()



