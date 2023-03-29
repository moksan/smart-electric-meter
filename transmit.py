from message_processing import *
from serial_processing import *

#from binascii import hexlify
#from watchdog import wdTimer


baud = [300 ,9600]
#startInitilizationReadoutSequence(baud[0])

#startReadoutSequence(baud[1])

startInitilizationProgModeSequence(baud[0])

startReadObisSequence(baud[1])


# print ('Initial: ' + readData)
# #print ('Meter ID: ' + hexlify(readData))
# print ('length: ' + str(len(readData)))
# #except  :
# #	print ("No chars received")	



