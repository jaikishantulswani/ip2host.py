import fileinput
import socket

RED = '31'
BLUE = '34'

def color(color_code, text):
    return '\033[{}m{}\033[0m'.format(color_code, text)

for line in fileinput.input():
    for ip in line.split():
        try:
            socket.inet_aton(ip)
        except Exception as invalid_ip:
            print color(RED, 'Invalid IP address = ') + ip
        else:
            hostname = socket.getfqdn(ip)
            print color(BLUE, ip) + ' hostname is ' + color(BLUE, hostname)
