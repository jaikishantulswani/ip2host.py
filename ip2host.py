#!/usr/bin/python
import socket
with open('ip.txt') as ipfile:
	for IP in ipfile:
		try:
			host = socket.getfqdn(IP)
			print host, IP.strip()
		except Exception, e:
			print e
