#!/usr/bin/python
import socket

def check_ip():
	try:
		socket.inet_aton(IP) # check for valid ipv4 address
	except Exception, e:
		print "Given list do not have valid list of ipv4 addresses."
		print "Invalid ip addresss = " + str(IP)
		exit()

with open('ip.txt') as ipfile:
	for IP in ipfile:
		check_ip()
		host = socket.getfqdn(IP)
		print host, IP.strip()
