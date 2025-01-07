# This will be just for educational purposes
# Credits to NeuraNine

'''
Port Scanners are primarily used for Penetration Testing and Information Gathering
I will be just practicing how to scan ports using my own network 

Basic Functionality
 - A port scanner tries to connect to an IP-Address on a certain port. Usually when we
 surf the web, we connect to servers via port 80 (HTTP) or port 43 (HTTPS).
  But there are also a lot of other crucial ports like 21 (FTP), 22 (SSH), 25 (SMTP) 
  and many more. In fact, there are more than 130,000 ports of which 1,023 are standardized 
  and 48,128 reserved. So, when we build a port scanner, we better make it efficient and focus
  on the crucial ports.
'''

# Simplest Way to scan ports

import socket

target = '127.0.0.1' # Local Machine IP Address

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

# print(portscan(80))

for port in range(1, 1024):
    result = portscan(port)
    if(result):
        print("Port {} is open!".format(port))
    else:
        print("Port {} is closed!".format(port))