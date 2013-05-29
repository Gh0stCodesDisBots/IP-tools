


#-------------------------------------------------------------------------------
# Name:        IP tools
# Purpose:     To make a few tools that assist in networking
#
# Author:      <4sec>
#
# Created:     29/05/2013
# Licence:     <Opensource GNU>
#-------------------------------------------------------------------------------

import urllib2, socket
from dns.exception import *
from time import sleep

def reverse_dnslookup(host):
    '''Get website ip address'''
    try :
        addr = socket.gethostbyname(host)
        print'IP address is : ',addr
        sleep(2)
        main()
    except Timeout:
        print'[*] The attempt to connect timed-out'
        if raw_input('Retry? (y) (n)') == 'y':
            reverse_dnslookup(host)
        else:
            menu()

def whatismyip():
    '''Find your own ip address by opening a whatismyip website'''
    try:
        ip = urllib2.urlopen('http://whatismyip.akamai.com/', timeout=10).read()
        print'\nYour ip address is ',ip
        print'\n'
        sleep(2)
        menu()

    except Timeout:
        print'[*] The attempt to connect timed-out'
        if raw_input('Retry? (y) (n)') == 'y':
            reverse_dnslookup(host)
        else:
            menu()

def menu():
    print'\n\n\t','='*30
    print'\t1. Find ip of a website'
    print'\t2. Find your own ip address'
    print'\n\t0. Exit'
    print'\t','='*30
    choice = raw_input('\n : ')
    if choice == '1':
        hostname = raw_input('\nEnter host name : ')
        reverse_dnslookup(hostname)
    elif choice == '2':
        whatismyip()
    elif choice == '0':
        exit()

if __name__ == '__main__':
    menu()

