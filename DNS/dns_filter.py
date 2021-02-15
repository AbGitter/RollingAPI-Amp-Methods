#!/usr/bin/env python
#Basic Threaded DNS Filter
#by K-Metal
 
 
import sys
import os
import time
import socket
import threading
 
# Check args
if len(sys.argv) < 4:
    print "Usage: <input> <output> <mx size>"
    sys.exit()
 
RUNNING = True
 
''' Customize '''
THREADS = 20
TIMEOUT = 0.05 #secs
PORT    = 53
BUFFER  = 65500
 
# [root] dns recursive payload
payload = "\x23\x61\x01\x20\x00\x01\x00\x00\x00\x00\x00\x01\x03\x31\x78\x31\x02\x63\x7a\x00\x00\xff\x00\x01\x00\x00\x29\x10\x00\x00\x00\x00\x00\x00\x00"
#payload = "\xc4\x75\x01\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\xff\x00\x01\x00\x00\x29\x23\x28\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
 
 
# split input list into thread chunks
def chunklist(l, n):
    parts = len(l) / n
    for i in xrange(0, len(l), parts):
        yield l[i:i+parts]
 
with open(sys.argv[1],'r') as f:
    data = f.read().splitlines()
    SIZE = len(data)
    CHUNKS = list(chunklist( data, THREADS ))
    print len(CHUNKS)
 
output = open( sys.argv[2], 'w' )
 
### Logger thread ###
logs = []
def log(msg):
    global logs
    logs.append( msg )
 
def logger_thread():
    global logs, output
    while True:
        time.sleep(0.1)
        if logs != []:
            log_data = str(logs.pop(-1))
            print log_data
            output.write( log_data.split()[0]+'\n' )
 
# Scan dns list #
def scanner(scan_list):
    global payload, TIMEOUT, PORT, RUNNING
 
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.settimeout( TIMEOUT )
    pkt_size = len(payload) + 28 #udp pkt hdr min size
 
    for ip in scan_list:
        try: 
            ip = str(socket.gethostbyname(ip))
 
            if RUNNING:
                sock.sendto( payload, (ip, PORT))
            else:
                break
 
            try:
                recvdata, addr = sock.recvfrom( BUFFER )
                ip_addr = str(addr[0])
                if len(recvdata) > int(sys.argv[3]): #sucess
                    amp = len(recvdata) / pkt_size*1.0
                    amp = round( amp, 2 )
                    log(
                        "{} {} [x{}]".format(ip_addr,len(recvdata),amp)
                        )
            except:
                pass
        except:
            pass
 
## Create threads ###
def create_thread(function, *args):
    thread = threading.Thread(target=function,args=args)
    thread.daemon = True
    thread.start()
    return thread
 
if __name__ == '__main__':
    # create logging thread
    create_thread(logger_thread)
 
    print "Started Scanning "+str(SIZE)+" targets"
 
    # create threads
    thread_list = []
    for t in CHUNKS:
        thread = create_thread( scanner, t )
        thread_list.append( thread )
 
    # wait for threads to end
    print "ThreadCount: " + str(threading.active_count())
    for t in thread_list:
        try:
            t.join()
        except KeyboardInterrupt:
            RUNNING = False
            break
 
    output.close()
    if 'nt' not in os.name:
        # for unix systems
        os.system("chmod 0777 "+str(sys.argv[2]))
 
    sys.exit()