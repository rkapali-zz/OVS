__author__ = 'bugtraq'

import default_values
import urllib2
import nmap
from conf_loader.server_auditor_conf import conf


# standard for the network configuration
ok = " .......................................[OK]"
warning = " .......................................[WARNING]"


# local_ip_resource = conf.get("network.local_ip_resource")
# public_ip_resource = conf.get("network.public_ip_resource")
# private_ip_resource = conf.get("network.private_ip_resource")
valid_tcp_port_list_lo = conf.get("network.valid_tcp_port_list_lo")
valid_tcp_port_list_eth0 = conf.get("network.valid_tcp_port_list_eth0")
valid_tcp_port_list_pub = conf.get("network.valid_tcp_port_list_pub")

# end of the network configuration standard

nmap_port_scanner = nmap.PortScanner()

def get_ip(resource):
    response = urllib2.urlopen(resource)
    ip_address = response.read()
    print "The IP address scanning: "+ ip_address
    return ip_address

def scan_ip(ip_address):

    tcp_port_list = []
    try:
        print "Scanning IP: ", ip_address
        nmap_port_scanner.scan(ip_address)
        open_ports = nmap_port_scanner[ip_address]['tcp']
        #print open_ports
        print "ports" + " " + "State" + " " + "Version" + " " + "Service"
        for rows in open_ports:
            port_number =  str(rows)

               # print "key = %s %s %s" % open_ports[rows]['state'],open_ports[rows]['version'], open_ports[rows]['name']
            print port_number + " " + open_ports[rows]['state'] + " " + open_ports[rows]['version'] + " " + open_ports[rows]['name']
            tcp_port_list.append(port_number)
        print tcp_port_list
        return tcp_port_list

    except OSError as oserror:
            print "Error has occured in scanIP method " + " " + oserror
            exit(200)

def compare_port_tcp_lo(tcp_port_list):
    #print tcp_port_list
    for value in tcp_port_list:
        if value not in valid_tcp_port_list_lo:
            print 'Port Standard for ' + value + " mismatched " + warning #print " " #'Port Standard for  ' + value + " matched " + ok
        # else:
        #     print 'Port Standard for ' + value + " mismatched " + warning

def compare_port_tcp_eth0(tcp_port_list):
    #print tcp_port_list
    for value in tcp_port_list:
        if value not in valid_tcp_port_list_eth0:
            print 'Port Standard for ' + value + " mismatched " + warning #print " " #'Port Standard for  ' + value + " matched " + ok
        # else:
        #     print 'Port Standard for ' + value + " mismatched " + warning

def compare_port_tcp_pub(tcp_port_list):
    #print tcp_port_list
    for value in tcp_port_list:
        if value not in valid_tcp_port_list_pub:
            print 'Port Standard for ' + value + " mismatched " + warning #print " " #'Port Standard for  ' + value + " matched " + ok
        # else:
        #     print 'Port Standard for ' + value + " mismatched " + warning

def scan_local_ip():
    compare_port_tcp_lo(scan_ip(default_values.AWS_LOCAL_IP))
    print("End of scanning Local IP")
    print " "

def scan_private_ip():
    compare_port_tcp_eth0(scan_ip(get_ip(default_values.AWS_PRIVATE_IP)))
    print("End of scanning Private IP")
    print " "

def scan_public_ip():
    compare_port_tcp_pub(scan_ip(get_ip(default_values.AWS_PUBLIC_IP)))
    print("End of scanning Public IP")
    print " "

def run_port_checker():
    scan_local_ip()
    scan_private_ip()
    scan_public_ip()
    print (" ............. END of the Port Scanning ................")


