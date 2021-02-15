#!usr/bin/python
import socket
import sys
 
if len(sys.argv) < 2:
    print 'Usage: <input> <output> <protocol> <min resp>'
    print 'Protocols: chargen, ntp, quake, ssdp, tftp, ts3, netbios, mdns, rip'
    sys.exit()
    
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.settimeout(0.05)
 
chargen = 'A'
ntp = '\x17\x00\x03\x2a\x00\x00\x00\x00'
quake = '\xFF\xFF\xFF\xFF\x67\x65\x74\x73\x74\x61\x74\x75\x73\x10'
ssdp = "M-SEARCH * HTTP/1.1\r\nHOST: 239.255.255.250:1900\r\nMAN: \"ssdp:discover\"\r\nMX: 2\r\nST: ssdp:all\r\n\r\n"
tftp = '\x00\x01\x2f\x78\x00\x6e\x65\x74\x61\x73\x63\x69\x69\x00'
ts3 = '\xff\xff\xff\xff\x67\x65\x74\x73\x74\x61\x74\x75\x73\x0a'
netbios = '\xe5\xd8\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x20\x43\x4b\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x00\x00\x21\x00\x01'
mdns = '\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x09\x5F\x73\x65\x72\x76\x69\x63\x65\x73\x07\x5F\x64\x6E\x73\x2D\x73\x64\x04\x5F\x75\x64\x70\x05\x6C\x6F\x63\x61\x6C\x00\x00\x0C\x00\x01'
rip = '\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10'
 
file1 = sys.argv[1]
file2 = sys.argv[2]
proto = sys.argv[3]
size = int(sys.argv[4])
 
with open(file1) as f:
    list = f.read().splitlines()
    
newfile = open(file2, 'w')
 
if proto == 'ntp':
    port = 123
    payload = ntp
    
elif proto == 'chargen':
    port = 19
    payload = chargen
    
elif proto == 'quake':
    port = 27960
    payload = quake
 
elif proto == 'ssdp':
    port = 1900
    payload = ssdp
    
elif proto == 'tftp':
    port = 69
    payload = tftp
 
elif proto == 'ts3':
    port = 9987
    payload = ts3
 
elif proto == 'netbios':
    port = 137
    payload = netbios
 
elif proto == 'mdns':
    port = 5353
    payload = mdns
 
elif proto == 'rip':
    port = 520
    payload = rip
 
else:
    print 'Protocol is not available'
    sys.exit()
 
c = 0
 
while c < len(list):
    s.sendto(payload, (list[c].split(' ',1)[0], port))
    
    try:
        data, addr = s.recvfrom(65500)
        if len(data) >= size:
            print addr[0]+' '+str(len(data))
            newfile.write(addr[0]+' '+str(len(data))+'\n')
            
    except Exception and socket.error and socket.timeout:
        I = 0
    c += 1
 
newfile.close()
 
with open(file2) as e:
    count = e.read().splitlines()
    
print 'Finished Filter saved to %s with %i lines' % ( file2,len(count) )