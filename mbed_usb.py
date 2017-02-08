import serial
import socket

s=socket.socket()
# ip of computer on which this file is listening
host= '127.0.0.1' 
port=12395
s.bind((host,port))
s.listen(5)

ser=serial.Serial()
ser.baudrate=115200
ser.timeout=1
ser.port='/dev/ttyACM0'

def touch_sensor():
   
	if ser.isOpen():
		try:
			test=0
			data=ser.readline()
			if data and int(data)>test:
				test=int(data)
				
			else:
				data2=ser.readline()
				if data2 and int(data2)>test:
					test=int(data2)
				else:
					data3=ser.readline()
					if data3 and int(data3)>test:
						test=int(data3)
					else:
						
						data4=ser.readline()
						if data4 and int(data4)>test:
							test=int(data4)
	
			ser.close()
			return str(test)
			
              
		except:
			pass
def touch_sensor2():
   
	if ser.isOpen():
		try:
			data=ser.readline()
			data2=ser.readline()
			data3=ser.readline()
			data4=ser.readline()
			if data or data2 or data3 or data4: 
				print "data"+ data
				print "data2"+ data2
				print "data3"+ data3
				print "data4"+ data4
				ser.close()
				return 1
			
			print '0'
			return 0
              
		except:
			pass


while True:
	c,addr=s.accept()
	data = c.recv(1024)
	print('Got connection from',addr)
	r=str(0)
	if ser.isOpen()==False:
	  ser.open()
	if data=='1':
		r=touch_sensor()
	else:
		r=touch_sensor2()
	print 'r='+str(r)
	ser.close()
	c.send(str(r))
	c.close()
