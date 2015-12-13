#!/usr/bin/python

import socket
import sys

BLUE='\033[34m'
RED='\033[31m'
NORMAL='\033[0m'

def check_ip():
        try:
                socket.inet_aton(ip)
        except Exception, e:
                print RED+"Given list do not have valid list of ipv4 addresses."
                print "Invalid ip addresss = "+NORMAL + str(ip)
                exit()

file = sys.argv[1]
with open(file) as ipfile:
        for iplist in ipfile:
                for IP in iplist.split():
                        ip = IP.strip(' \t\n\r')
                        if ip == '':
                                pass
                        else:
                                check_ip()
                                host = socket.getfqdn(ip)
                                print BLUE+ip+NORMAL + " hostname is " + BLUE+host+NORMAL
