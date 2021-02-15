#K-Metal's Chargen Filter v2
#Better layout
#You can change the payload for and UDP method of your choice
 
import socket
import sys
 
if len(sys.argv) < 2:
	print "Usage: <input> <output> <mx size>"
	print "You can change timeout in script"
	sys.exit()
 
#Getting our variables set
file1 = sys.argv[1]
file2 = sys.argv[2]
size = int(sys.argv[3])
 
#UDP packet and timeout
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(0.05)	#CHANGE TIMEOUT HERE
 
#count for the list, sent bytes, found IPs, and received bytes
count = 0
found = 0
sent = 0
received = 0
 
#Read the list and open a new file to write to
with open(file1) as f:
	list = f.read().splitlines()
newfile = open(file2, "w")
 
print "Found\t\tSent Byts\tRecv Byts"
 
#Commence the scan!
while count < len(list):
	a = list[count].split(" ",1)[0] #Make sure to only get the IP
	s.sendto("A", (a, 19)) #Send chargen packet
 
	sent += 43 	#send = itself + 43(bytes in chargen packet)
 
	try:	#Listen for response
		data, addr = s.recvfrom(655000)
		received += int(len(data))
 
		if int(len(data)) > size:
			#write the IP found to file
			newfile.write(str(addr[0])+" "+str(len(data))+"\n")
			found += 1
	except socket.timeout and socket.error:
		notfound = "Yup"
 
	sys.stdout.write("\r|%i\t\t|%i\t\t|%i" % (found, sent, received) )
	sys.stdout.flush()
 
	count += 1
 
newfile.close()
 
print "\nScan finished and saved to %s" % (file2)