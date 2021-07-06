#!/bin/python

import sys
import socket
from datetime import datetime

#Creates a log of opened ports
def save(ip, ports):
	print("Total found ports: " + str(len(ports)))
	sys.stdout = open("scanns.log", "a")
	print("(" + str(datetime.now()) + ") " + str(ip) + ": " + str(ports))
	sys.stdout.close()

#Check args
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid input.")
	print("Sytax: python3 scanner.py <ip>")
	sys.exit()

#Banner
print("#" * 50)
print("Scannig target " + target)
print("Time started: " + str(datetime.now()))
print("#" * 50)
print("\n")

#Starts the scan
try:
	opened = []
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.001)
		result = s.connect_ex((target,port))
		div = int(port * 100 / 65535)
		print("Scanned ports: {}%".format(div), end="\r")
		if result == 0:
			opened.append(port)
			print("Port {} is open".format(port))
		s.close()

	#Ends the program
	print("\n\nScan finished on " + str(datetime.now()))
	save(target, opened)
	sys.exit()


#Exceptions
except KeyboardInterrupt:
	print("\n\nExiting program...")
	if s:
		s.close()
	save(target, opened)
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()

except socket.error:
	print("Unable to connect to server")
	sys.exit()