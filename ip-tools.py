#-------------------------------------------------------------------------------
# Name:        IP tools
# Purpose:     To make a few tools that assist in networking
#
# Author:      <4sec>
#
# Created:     29/05/2013
# Licence:     <Opensource GNU>
#-------------------------------------------------------------------------------

import urllib2
import socket
from time import sleep

def find_ip_of_website(host):
    addr = socket.gethostbyname(host)
    print'IP address is : ',addr
    sleep(2)
    main()

def whatismyip():
    ip = urllib2.urlopen('http://whatismyip.akamai.com/', timeout=10).read()
    print'\nYour ip address is ',ip
    print'\n'
    sleep(2)
    main()

def main():
    print'\n\n\t','='*30
    print'\t1. Find ip of a website'
    print'\t2. Find your own ip address'
    print'\t','='*30
    print'\n\n\t0. Exit'
    choice = raw_input('\n : ')
    if choice == '1':
        hostname = raw_input('\nEnter host name : ')
        find_ip_of_website(hostname)
    elif choice == '2':
        whatismyip()
    elif choice == '0':
        exit()

main()

