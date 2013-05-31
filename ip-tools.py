#-------------------------------------------------------------------------------
# Name:        IP tools
# Purpose:     To make a few tools that assist in networking
#
# Author:      <4sec>
#
# Created:     29/05/2013
# Licence:     <Opensource GNU>
#-------------------------------------------------------------------------------

import urllib2, socket, sys
from dns.exception import *
from time import sleep

def usage():
    print'''
    Usage:
        IP-tools.py -u <url>    you can include http:// and / or not.
        IP-tools.py -o          View your own ip address
    '''

def reverse_dnslookup(host):
    '''Get website ip address'''
    try :
        if '/' in host : host = host.replace('/','')
        if 'http:' in host : host = host.replace('http:','')
        addr = socket.gethostbyname(host)
        print''
        print'+'+'='*32 +'+'
        print'|IP address is : ',addr,'|'
        print'+'+'='*32 +'+'

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
        print''
        print'+'+'='*33 +'+'
        print'|Your ip address is ',ip,'|'
        print'+'+'='*33 +'+'
        print'\n'
        sleep(2)

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
        if hostname.endswith('/'):
            hostname = hostname.replace('/','')
            if hostname.startswith('http:'): hostname = hostname.replace('http:','')
        elif hostname.startswith('http:'):
            hostname = hostname.replace('http:','')
            if hostname.endswith('/'):
                hostname = hostname.replace('/','')
        else:
            pass
        reverse_dnslookup(hostname)
    elif choice == '2':
        whatismyip()
        sleep(2)
        menu()
    elif choice == '0':
        exit()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '-u':
            host = sys.argv[2]
            reverse_dnslookup(host)
        elif sys.argv[1] == '-o':
            whatismyip()
        else:
            usage()
    else:
        menu()
