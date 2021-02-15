#!/bin/bash
#    BOOTER.SU - AutoScanner & Filter
#    Script Installer: http://pastebin.com/zPJpQrbW
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    Available Methods to Scan:
#      NTP
#      SSDP 
#      DNS 
#      CHARGEN 
#      SNMPv2 
#      Sentinel 
#      NetBIOS 
#      MSSQL 
#      TS3 
#      PORTMAP 
#
#
#    2016-05-03: Initial version, tested with Ubuntu 15.04
 
if [ $# != 1 ]; then
echo "BOOTER.SU - AutoScanner & Filter"
echo "Usage: $0 [OPTION]"
echo "Option: -ntp (Scan for NTP Amps)"
echo "Option: -ssdp (Scan for SSDP Amps)"
echo "Option: -dns (Scan for DNS Amps)"
echo "Option: -chargen (Scan for CHARGEN Amps)"
echo "Option: -snmp (Scan for SNMPv2 Amps)"
echo "Option: -sentinel (Scan for Sentinel Amps)"
echo "Option: -netbios (Scan for NetBIOS Amps)"
echo "Option: -mssql (Scan for MSSQL Amps)"
echo "Option: -ts3 (Scan for TS3 Amps)"
echo "Option: -portmap (Scan for PORTMAP Amps)"
echo "Option: -h (Help)"
exit 0
fi
 
while test $# -gt 0; do
        case "$1" in
                -ntp)
                echo "IPv4 Range? (START END): "
                read range
                echo "Starting NTP Scan...."
                amp/ntpscan $range amplists/ntp-og.txt 4 10
                cd amplists
                echo "Filtering..."
                cat ntp-og.txt | sort -u > unique.txt
                cat unique.txt | awk '{print $1}' | sort -u | sort -R > ntp.txt
                rm -rf unique.txt
                ls -l 
                cd ..
                exit 0
                        ;;
                -ssdp)
                echo "IPv4 Range? (START END): "
                read range
                echo "Starting SSDP Scan...."
                amp/ssdpscan $range amplists/ssdp-og.txt 4 10
                cd amplists
                echo "Filtering..."
                cat ssdp-og.txt | sort -u > unique.txt
                cat unique.txt | awk '{print $1}' | sort -u | sort -R > ssdp.txt
                rm -rf unique.txt
                ls -l 
                cd ..
                exit 0
                        ;;
                -dns)
                echo "IPv4 Range? (START END): "
                read range
                echo "Starting DNS Scan...."
                amp/dnsscan $range amplists/dns-og.txt 4 10
                cd amplists
                echo "Filtering..."
                cat dns-og.txt | sort -u > unique.txt
                cat unique.txt | awk '{print $1}' | sort -u | sort -R > dns.txt
                rm -rf unique.txt
                ls -l 
                cd ..
                exit 0
                        ;;
                -chargen)
                echo "IPv4 Range? (START END): "
                read range
                echo "Starting CHARGEN Scan...."
                amp/chargenscan $range amplists/chargen-og.txt 4 10
                cd amplists
                echo "Filtering..."
                cat chargen-og.txt | sort -u > unique.txt
                cat unique.txt | awk '{print $1}' | sort -u | sort -R > chargen.txt
                rm -rf unique.txt 
                ls -l 
                cd ..
                exit 0
                        ;;
                -snmp)
                echo "IPv4 Range? (START END): "
                read range
                echo "Starting SNMP Scan...."
                amp/snmpscan $range amplists/snmp-og.txt 4 10
                cd amplists
                echo "Filtering..."
                cat snmp-og.txt | sort -u > unique.txt
                cat unique.txt | awk '{print $1}' | sort -u | sort -R > snmp.txt
                rm -rf unique.txt
                ls -l 
                cd ..
                exit 0
                        ;;
                -sentinel)
                echo "IPv4 Range? (START END): "
                read range
                echo "Starting Sentinel Scan...."
                amp/sentinelscan $range amplists/sentinel-og.txt 4 10
                cd amplists
                echo "Filtering..."
                cat sentinel-og.txt | sort -u > unique.txt
                cat unique.txt | awk '{print $1}' | sort -u | sort -R > sentinel.txt
                rm -rf unique.txt
                ls -l 
                cd ..
                exit 0
                        ;;
                -netbios)
                echo "IPv4 Range? (START END): "
                read range
                echo "Starting NetBIOS Scan...."
                amp/netbiosscan $range amplists/netbios-og.txt 4 10
                cd amplists
                echo "Filtering..."
                cat netbios-og.txt | sort -u > unique.txt
                cat unique.txt | awk '{print $1}' | sort -u | sort -R > netbios.txt
                rm -rf unique.txt
                ls -l 
                cd ..
                exit 0
                        ;;
                -mssql)
                echo "IPv4 Range? (START END): "
                read range
                echo "Starting MSSQL Scan...."
                amp/mssqlscan $range amplists/mssql-og.txt 4 10
                cd amplists
                echo "Filtering..."
                cat mssql-og.txt | sort -u > unique.txt
                cat unique.txt | awk '{print $1}' | sort -u | sort -R > mssql.txt
                rm -rf unique.txt
                ls -l 
                cd ..
                exit 0
                        ;;
                -ts3)
                echo "IPv4 Range? (START END): "
                read range
                echo "Starting TS3 Scan...."
                amp/ts3scan $range amplists/ts3-og.txt 4 10
                cd amplists
                echo "Filtering..."
                cat ts3-og.txt | sort -u > unique.txt
                cat unique.txt | awk '{print $1}' | sort -u | sort -R > ts3.txt
                rm -rf unique.txt
                ls -l 
                cd ..
                exit 0
                        ;;
                -portmap)
                echo "IPv4 Range? (START END): "
                read range
                echo "Starting PORTMAP Scan...."
                amp/portmapscan $range amplists/portmap-og.txt 4 10
                cd amplists
                echo "Filtering..."
                cat portmap-og.txt | sort -u > unique.txt
                cat unique.txt | awk '{print $1}' | sort -u | sort -R > portmap.txt
                rm -rf unique.txt
                ls -l 
                cd ..
                exit 0
                        ;;
                -h|--help)
                    echo "BOOTER.SU - AutoScanner & Filter"
                    echo "Option: -ntp (Scan for NTP Amps)"
                    echo "Option: -ssdp (Scan for SSDP Amps)"
                    echo "Option: -dns (Scan for DNS Amps)"
                    echo "Option: -chargen (Scan for CHARGEN Amps)"
                    echo "Option: -snmp (Scan for SNMPv2 Amps)"
                    echo "Option: -sentinel (Scan for Sentinel Amps)"
                    echo "Option: -netbios (Scan for NetBIOS Amps)"
                    echo "Option: -mssql (Scan for MSSQL Amps)"
                    echo "Option: -ts3 (Scan for TS3 Amps)"
                    echo "Option: -portmap (Scan for PORTMAP Amps)"
                    exit 0
                        ;;
                *)
                    echo "Invalid Option. Exiting."
                    exit 0
                        ;;
        esac
done