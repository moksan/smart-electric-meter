import select
import time

import serial

from utilities import *


def openConnection(baudrate):
    try:
        global Rs485
        Rs485 = serial.Serial()
        Rs485.port = '/dev/ttyUSB0'						# set interface instance
        Rs485.baudrate = baudrate					# set baudrate to 300
        Rs485.parity = serial.PARITY_EVEN			        # set parity to even parity
        Rs485.bytesize = serial.SEVENBITS			        # number of bits per byte
        Rs485.stopbits = serial.STOPBITS_ONE		                # number of stop bits
        Rs485.timeout = None						# block read
        #Rs485.timeout = 0						# non-block read
        #Rs485.timeout = 1						# timeout block read -set to 50ms to start with (value for 300bd)
        Rs485.xonxoff = False						# disable software flow control - same as handshake ???
        #Rs485.rs485_mode =serial.rs485.RS485Settings()
        Rs485.rtscts = False						# disable hardware (RTS/CTS) flow control
        Rs485.dsrdtr = False						# disable hardware (DSR/DTR) flow control
        Rs485.writeTimeout = 0					        # timeout for write
        Rs485.interCharTimeout = 0				        # timeout between bytes - doesn't seem to work ???

        Rs485.open()
        connected = True

    except select.error:
        connected = False
    return connected    

def closeConnection():
    global connected
    try:
        Rs485.close()
        connected  = False
    except:
        pass

def readPort_a():
        Rs485.flushInput()
        readBuffer  = ''
        readBytes = ''
        while ('' == readBuffer):
            readBuffer = Rs485.read(1)			# poll for 1st received byte
            time.sleep(0.025)			        # polling sample time (25ms)

        while (readBuffer.isspace() != True ):
                readBytes +=  str(readBuffer.decode())	# build received message
                readBuffer = Rs485.read(1)	        # read 1 byte at a time

        return readBytes

def readPort_b(size):
        Rs485.flushInput()
        line = []

        while True:
            for c in Rs485.read(size):
                line.append(c)
                if c == b'\x03':
                    print("Line: " + ''.join(line))
                    line = []
                    break

            return line

def identification_electric_meter():
        print ('sending: / ? ! CR LF')
        Rs485.write(b'/?!\r\n')
        #time.sleep(0.25)						

def terminate_comm_code():
        print ('sending: SOH B 0 ETX BCC') # BCC ---> q(0x71)
        command = b'\x01\x42\x30\x03\x71' 
        Rs485.write(command)
        print(command)
        time.sleep(0.25)						

def initilization_comm_baudrate(z):
        print ('sending: ACK 0 Z 7 CR LF')
        #Rs485.write(b''ACK'057\r\n') 
        #baud = BAUDRATE[z]
        # base16INT = int(BAUDRATE[z],16)
        # hex_value = hex(base16INT)        
        # command = [x06,x30,x37,x0d,x0a]        
        # command.insert(2,hex_value)
        
        command = b'\x06\x30\x35\x37\x0d\x0a' 
        time.sleep(0.25)						
        Rs485.write(command)
        #print(command)
        time.sleep(0.25)	

def initilization_prog_mode(z):
        print ('sending: ACK 0 Z 1 CR LF')
        command = b'\x06\x30\x35\x31\x0d\x0a' 
        time.sleep(0.25)						
        Rs485.write(command)
        #print(command)
        time.sleep(0.25)    

def writePort_T(): #TODO: Obis codu için dönüşüm yapılacak
        print ('sending: 1.8.0')
        Rs485.write(b'\x01\x52\x32\x02\x31\x2e\x38\x2e\x30\x28\x29\x03\x59')
        #time.sleep(0.25)    

def writePort_T1(): #TODO: Obis codu için dönüşüm yapılacak
        print ('sending: 1.8.1')
        Rs485.write(b'\x01\x52\x32\x02\x31\x2e\x38\x2e\x31\x28\x29\x03\x58')
        #time.sleep(0.25)  

def writePort_T2(): #TODO: Obis codu için dönüşüm yapılacak
        print ('sending: 1.8.2')
        Rs485.write(b'\x01\x52\x32\x02\x31\x2e\x38\x2e\x32\x28\x29\x03\x5b')
        #time.sleep(0.25)  
        
def writePort_T3(): #TODO: Obis codu için dönüşüm yapılacak
        print ('sending: 1.8.3')
        Rs485.write(b'\x01\x52\x32\x02\x31\x2e\x38\x2e\x33\x28\x29\x03\x5a')
        #time.sleep(0.25)       
                   
def writePort_T4(): #TODO: Obis codu için dönüşüm yapılacak
        print ('sending: 1.8.4')
        Rs485.write(b'\x01\x52\x32\x02\x31\x2e\x38\x2e\x34\x28\x29\x03\x5d')
        #time.sleep(0.25)        