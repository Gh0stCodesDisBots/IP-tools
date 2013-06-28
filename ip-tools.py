#-------------------------------------------------------------------------------
# Name: IP tools
# Purpose: To make a few tools that assist in networking
#
# Author: <4sec>
# Created: 29/05/2013
# Licence: <Opensource GNU>
#-------------------------------------------------------------------------------

import urllib2, socket, sys, random,urllib
from time import sleep
from sys import stdout
from time import sleep

def output(text,speed=''):
    for char in text:
        stdout.write(char)
        stdout.flush()
        if speed == '':
            t = [0.01,0.02]
            time = random.choice(t)
            sleep(time)
        else:
            sleep(speed)

def usage():
    try:
        output('''
    Usage:
    IP-tools.py -h      -Show this help message
    IP-tools.py -o      -View your own ip address
    IP-tools.py -u <url>-View ip address of a website
    IP-tools.py         -Go to program menu
    IP-tools.py -p      -Go to portscan section
    IP-tools.py -p <ip> -Scan that ip for open ports.
                        You can specify the port range too
    IP-tools.py -p <ip> <port-range> -Scan that ip for open ports from 5 to 100.
    IP-tools.py -info <url/ip> -Get info about the server.
Example:

    IP-tools.py -u http://www.google.com/
    IP-tools.py -u www.google.com
    IP-tools.py -p 127.0.0.1
    IP-tools.py -p 127.0.0.1 5-100
    IP-tools.py -info www.google.com
''')
    except KeyboardInterrupt:
        output('\n\t[!] User interrupt\n\t[!] Program terminated')
        exit()

def reverse_dnslookup(host):
    '''Get website ip address'''
    try :
        if '/' in host : host = host.replace('/','')
        if 'http:' in host : host = host.replace('http:','')
        addr = socket.gethostbyname(host)
        print''
        print'+'+'='*32 +'+'
        print'|IP address is : ',addr
        print'+'+'='*32 +'+'

    except KeyboardInterrupt:
        output('\n\t[!] User interrupt')
        output('\n\t[!] Program terminated ')
        exit()

def whatismyip():
    '''Find your own ip address by opening a whatismyip website'''
    try:
        ip = urllib2.urlopen('http://whatismyip.akamai.com/', timeout=10).read()
        print''
        banner1 = '+'+'='*33 +'+'
        output(banner1)
        print'\n|Your ip address is ',ip
        output(banner1,'')
        print'\n'
        sleep(2)

    except KeyboardInterrupt:
        output('\n\t[!] User interrupt')
        output('\n\t[!] Program terminated ')
        exit()

def server_info(site):
    if site == '':
        output('\nEnter server address')
        site = raw_input(' : ')
    if 'http://' not in site: site = 'http://' + site
    output('\n\t[*] Working on it ')
    try:
        url = urllib.urlopen(site)
        info = url.info()
        print'\n'
        banner1 = '+'+'='*33 +'+'
        output(banner1)
        print '\n%s' % info
        output(banner1,'')
        sleep(2)
        menu()

    except IOError:
        msg = '\n\t[!] Couldn\'t open %s' % site,'\n'
        output(msg,'')
        sleep(2)
        menu()
    except KeyboardInterrupt:
        output('\n\t[!] User interrupt')
        output('\n\t[!] Program terminated ')
        exit()

def menu():
    graphic = '''\n\n
/$$$$$$ /$$$$$$$        /$$$$$$$$                  /$$
|_  $$_/| $$__  $$      |__  $$__/                 | $$
  | $$  | $$  \ $$         | $$  /$$$$$$   /$$$$$$ | $$  /$$$$$$$
  | $$  | $$$$$$$/         | $$ /$$__  $$ /$$__  $$| $$ /$$_____/
  | $$  | $$____/          | $$| $$  \ $$| $$  \ $$| $$|  $$$$$$
  | $$  | $$               | $$| $$  | $$| $$  | $$| $$ \____  $$
 /$$$$$$| $$               | $$|  $$$$$$/|  $$$$$$/| $$ /$$$$$$$/
|______/|__/               |__/ \______/  \______/ |__/|_______/

                            (-) Uplink (-)'''
    output(graphic,0.0001)
    banner = '\n\n\t','='*30
    output(banner,'')
    output('\n\t| 1. Find ip of a website')
    output('\n\t| 2. Find your own ip address')
    output('\n\t| 3. Port Scanner')
    output('\n\t| 4. Server Info Digger')
    output('\n\n\t| 0. Exit')
    output(banner)

    try:
        choice = raw_input('\n : ')
        if choice == '1':
            output('\nEnter host name')
            hostname = raw_input(" : ")
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
        elif choice == '3':
            portrange = ''
            ip = ''
            port_scan(ip,portrange)
        elif choice == '4':
            output('\nEnter server address')
            site = raw_input(' : ')
            server_info(site)
        elif choice == '0':
            exit()
        else:
            output('\n\t[!] You need to enter a number not other thing')
            sleep(3)
            menu()
    except KeyboardInterrupt:
        output('\n\t[!] User interrupt\n\t[!] Program terminated')
        exit()

def port_scan(ip,portrange):
    try:
        if ip == '':
            output('Enter target ip address')
            ip = raw_input(' : ')
        if portrange == '' :
            output("Enter port range eg(5-200)")
            lowport,highport = raw_input(" : ").split('-')
        else:
          lowport,highport = portrange.split('-')
        msg = '[~] Scanning host ', ip,' from port ', lowport,' to port ',highport,' [~]\n'
        output(msg,'')

        for port in range(eval(lowport),eval(highport)+1):
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            status = s.connect_ex((ip,port))
            if (status ==0):
                opn = '\n========[1] Port '+str(port)+' -OPEN [1]========'
                output(opn)
            else:
                cld = '\n\t[0] Port '+str(port)+' -CLOSED [0]'
                output(cld)
            s.close()
        output('\n\nGreetingz from <4sec>\n','')

    except KeyboardInterrupt:
        output('\n\t[!] User interrupt','')
        output('\n\t[!] Program terminated ','')
        exit()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == '-o':
            whatismyip()
        elif sys.argv[1] == '-h' or sys.argv[1] == '-help':
            usage()
        elif sys.argv[1] == '-p':
            output('\n\t A simple port scanner\n\n')
            ip = ''
            portrange = ''
            port_scan(ip,portrange)
        elif sys.argv[1] == '-b' or sys.argv[1] == '-banner':
            site = ''
            server_info(site)
        else: usage()
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-u':
            host = sys.argv[2]
            reverse_dnslookup(host)
        elif sys.argv[1] == '-p':
            ip = sys.argv[2]
            port = ''
            port_scan(ip,port)
        elif sys.argv[1] == '-info':
            site = sys.argv[2]
            server_info(site)
        else:
            usage()

    elif len(sys.argv) == 3:
        if sys.argv[1] == '-p':
            ip = sys.argv[2]
            portrange = ''
            port_scan(ip,portrange)
    elif len(sys.argv) == 4 and sys.argv[1] == '-p':
        ip = sys.argv[2]
        portrange = sys.argv[3]
        port_scan(ip,portrange)
    else:
        menu()
