#!/usr/bin/python
import socket
import sys

def check_ip():
	try:
		socket.inet_aton(ip)
	except Exception, e:
		print "Given list do not have valid list of ipv4 addresses."
		print "Invalid ip addresss = " + str(ip)
		exit()

file = sys.argv[1]
with open(file) as ipfile:
	for IP in ipfile:
		ip = IP.rstrip('\r\n')
		if ip == '':
			pass
		else:
			check_ip()
			host = socket.getfqdn(ip)
			print host, ip
