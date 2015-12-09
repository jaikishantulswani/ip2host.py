#!/usr/bin/python
import socket
ipfile = open ('ip.txt')
while True:
    IP = ipfile.readline()
    try:
        host = socket.getfqdn(IP.rstrip())
        print host, IP
    except Exception, e:
        print "Unknown", IP 
        break 
ipfile.close()
