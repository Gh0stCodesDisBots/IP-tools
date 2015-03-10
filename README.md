IP-tools
========

This tool has four features currently:

  1. View ip address of a website
  2. View your own ip address
  3. Port Scan
  4. Server Info Dig
  
Usage:
------

	IP-tools.py -o                   -View your own ip address
	IP-tools.py -u <url>             -View ip address of a website
	IP-tools.py                      -Go to program menu
	IP-tools.py -p                   -Go to portscan section
	IP-tools.py -p <ip address>   	 -Scan that ip for open ports. You can specify the port range too
	IP-tools.py -p <ip> <port-rnage> -Scan that ip for open ports from 5 to 100.
	IP-tools.py -info <url/ip>       -View Server info from response header
  
Example:
-------- 
  
	IP-tools.py -u http://www.google.com/
	IP-tools.py -u www.google.com
	IP-tools.py -p 127.0.0.1
  	IP-tools.py -p 127.0.0.1 5-100
  	IP-toosl.py -info www.google.com  
