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

# Function to scan a single port on the target 
def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

# print(portscan(80))

# For loop to check for ports
# for port in range(1, 1024):
#     result = portscan(port)
#     if(result):
#         print("Port {} is open!".format(port))
#     else:
#         print("Port {} is closed!".format(port))
        

from queue import Queue # Queueing the port numbers, everytime I get a port, it will shift to a new one
import threading # For creating and managing threads

queue = Queue()
open_ports = []

# Function to fill the queue with port numbers from the given port list
def fill_queue(port_list):
    for port in port_list:
        queue.put(port) # Add each port in the list to the queue
        
# Worker function for threads to scan ports
def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)
        else:
            print("Port {} is closed!".format(port))
    

port_list = range(1, 104)
fill_queue(port_list) # Fill the queue with these ports 

thread_list = []

# Create 100 threads, each running the worker function 
for t in range(100):
    thread = threading.Thread(target=worker) # Creates a thread with target as the worker function 
    thread_list.append(thread)
    
# Start all threads
for thread in thread_list:
    thread.start()
    
# Wait for all threads to complete    
for thread in thread_list:
    thread.join()
    
print("Open ports are: ", open_ports)