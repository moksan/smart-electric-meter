
import serial
import time
from binascii import hexlify
from watchdog import wdTimer

ser = serial.Serial()

ser.port = '/dev/ttyUSB0'			# set interface instance
ser.baudrate = 300					# set baudrate to 9600
ser.parity = serial.PARITY_EVEN			# set parity to even parity
ser.bytesize = serial.SEVENBITS			# number of bits per byte
ser.stopbits = serial.STOPBITS_ONE		# number of stop bits
#ser.timeout = None				# block read
#ser.timeout = 0				# non-block read
ser.timeout = 0.25				# timeout block read -set to 50ms to start with (value for 300bd)
ser.xonxoff = False				# disable software flow control - same as handshake ???
ser.rtscts = False				# disable hardware (RTS/CTS) flow control
ser.dsrdtr = False				# disable hardware (DSR/DTR) flow control
ser.writeTimeout = 0				# timeout for write
ser.interCharTimeout = 0			# timeout between bytes - doesn't seem to work ???

ser.open()

print ('sending: / ? ! CR LF')
#ser.write("/?!\r\n")
#ser.write(str.encode("/?!\r\n"))
ser.write(0x2F); # "/"
ser.write(0x3F); # "?"
ser.write(0x21); # "!"
ser.write(0x0D); # "\r"
ser.write(0x0A); # "\n"
time.sleep(0.250)						# give write time to finish (34ms per char @ 300bd)

# 50ms after the write the meter sends the following:
#  /  F  M  l  4  A  0  0  0  0  V  8  0 CR LF
# 2f 46 4d 6c 34 41 30 30 30 30 56 38 30 0d 0a
#

def readPort():
	ser.flushInput()
	readBuffer  = ''
	readBytes = ''
	while ('' == readBuffer):
		readBuffer = ser.read(1)			# poll for 1st received byte
		time.sleep(0.025)					# polling sample time (25ms)
	while ('' != readBuffer):
		readBytes += readBuffer				# build received message
		readBuffer = ser.read(1)			# read 1 byte at a time
	return readBytes

try:
	with wdTimer(2):					# timeout of 2 seconds before 1st char received
		readData = readPort()
		print ('data read: ' + hexlify(readData))
		print ('length: ' + str(len(readData)))
except  :
	print ("No chars received")				# timeout tidying / error logging goes here

time.sleep(0.2)

print ('sending: SOH B 0 ETX q')
ser.write(str.encode("\x01B0\x03q"))
try:
	with wdTimer(2):					# timeout of 2 seconds before 1st char received
		readData = readPort()
		print ('data read: ' + hexlify(readData))
		print ('length: ' + str(len(readData)))
except  :
	print ("No chars received")				# timeout tidying / error logging goes here
time.sleep(0.2)

ser.close()