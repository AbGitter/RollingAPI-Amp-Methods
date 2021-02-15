#!/bin/bash
read -p "Select TCP, DNS or CHARGEN! " RESP
 
if [ "$RESP" = "TCP" ]; then
echo "Border Gateway Protocol Scanning started, for use of litespeeds TCP attack script"
 
##Edit the IPADDRESS below to your requested IP range
 
nmap -oG - -T4 -p179 -v 109.0.0.0-255 | grep "Ports: 179/filtered/tcp//bgp///" > temp1
echo "Checking Ip's and filtering"
grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' temp1 > temp2
sed -e 's/$/ 179/' -i temp2
cp temp2 TCP.txt
rm -rf temp*
killall -9 nmap
echo "Done!, Saved as TCP.txt"
 
elif [ "$RESP" = "CHARGEN" ]; then
echo "Chargen Service scanner. for use of litespeeds CHARGEN attack script"
 
##Change below...
 
nmap -sT -p 19 85.88.*.* -oG - | grep 19/open > temp
grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' temp > CHARGEN.txt
killall -9 nmap
echo "Saved list as CHARGEN.txt"
 
elif [ "$RESP" = "DNS" ]; then
echo "Starting DNS scan."
 
##Below edit the IP to your liking.
 
nmap 216.146.35.* --script=dns-recursion -sU -p53 > temp
grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' temp > DNS.txt
##sed 's/\(.*\)/\1 hackforums.net/' < DNS.txt > DNSd.txt
killall -9 nmap
echo "Saved list as DNS.txt"
 
else
  echo "Invalid input!"
fi