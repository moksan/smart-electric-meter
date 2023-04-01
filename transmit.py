#from binascii import hexlify
#from watchdog import wdTimer
from pypreprocessor import pypreprocessor

from message_processing import *
from serial_processing import *
from utilities import input_param
import time
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
startInitilizationProgModeSequence(input_param.BAUDRATE[0])
startReadObisSequence(input_param.BAUDRATE[1])
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



