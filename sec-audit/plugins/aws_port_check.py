__author__ = 'bugtraq'

import default_values
import urllib2
import nmap
from conf_loader.server_auditor_conf import conf


# variables used for HTML

ok = default_values.OK
warning = default_values.WARNING
error = default_values.ERROR
error = default_values.ERROR 
okstart = default_values.OKSTART 
okend = default_values.OKEND 
wrstart = default_values.WRSTART 
wrend = default_values.WREND 
erstart = default_values.ERSTART 
erend = default_values.EREND 
indstart = default_values.INDSTART 
indend = default_values.INDEND 
boldstart = default_values.BOLDSTART 
boldend = default_values.BOLDEND
br = default_values.BR

# ok = " .......................................[OK]"
# warning = " .......................................[WARNING]"


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
        print "Scanning IP: %s %s" %(ip_address,br)
        nmap_port_scanner.scan(ip_address)
        open_ports = nmap_port_scanner[ip_address]['tcp']
        #print open_ports
        #print """%s <table style="width:40%;"> <tr><td style="width:50px;max-width:50px;">ports</td>  <td style="width:50px;max-width:50px;">State</td> <td style="width:50px;max-width:50px;">Version</td> <td style="width:50px;max-width:50px;">Service </td></tr></table>%s""" %(indstart,indend)
        for rows in open_ports:
            port_number =  str(rows)
            if open_ports[rows]['version'] == "":
                open_ports[rows]['version'] = "N/A"
               # print "key = %s %s %s" % open_ports[rows]['state'],open_ports[rows]['version'], open_ports[rows]['name']
            #print """%s <table style="width:40%;"> <tr><td style="width:50px;max-width:50px;">%s</td> <td style="width:50px;max-width:50px;">%s</td> <td style="width:50px;max-width:50px;">%s</td> <td style="width:50px;max-width:50px;">%s</td></tr></table>%s""" %(indstart,port_number,open_ports[rows]['state'],open_ports[rows]['version'],open_ports[rows]['name'],indend)
            tcp_port_list.append(port_number)
        print "List of open ports: %s %s" %(tcp_port_list,br)
        return tcp_port_list

    except OSError as oserror:
            print "Error has occured in scanIP method " + " " + oserror
            exit(200)

def compare_port_tcp_lo(tcp_port_list):
    #print tcp_port_list
    for value in tcp_port_list:
        if value not in valid_tcp_port_list_lo:
            print "%sPort Standard for %s mismatched %s %s" %(wrstart,value,warning,wrend) #print " " #'Port Standard for  ' + value + " matched " + ok
            print " %s" %default_values.PORTRECOM
        # else:
        #     print 'Port Standard for ' + value + " mismatched " + warning

def compare_port_tcp_eth0(tcp_port_list):
    #print tcp_port_list
    for value in tcp_port_list:
        if value not in valid_tcp_port_list_eth0:
            print "%sPort Standard for %s mismatched %s %s " %(wrstart,value,warning,wrend) #print " " #'Port Standard for  ' + value + " matched " + ok
            print " %s" %default_values.PORTRECOM
        # else:
        #     print 'Port Standard for ' + value + " mismatched " + warning

def compare_port_tcp_pub(tcp_port_list):
    #print tcp_port_list
    for value in tcp_port_list:
        if value not in valid_tcp_port_list_pub:
            print "%sPort Standard for %s mismatched %s %s" %(wrstart,value,warning,wrend) #print " " #'Port Standard for  ' + value + " matched " + ok
            print " %s" %default_values.PORTRECOM
        # else:
        #     print 'Port Standard for ' + value + " mismatched " + warning

def scan_local_ip():
    compare_port_tcp_lo(scan_ip(default_values.AWS_LOCAL_IP))
    print("%s.............. End of scanning Local IP ..............") %br
    print " "

def scan_private_ip():
    compare_port_tcp_eth0(scan_ip(get_ip(default_values.AWS_PRIVATE_IP)))
    print("%s.............. End of scanning Private IP ..............")%br
    print " "

def scan_public_ip():
    compare_port_tcp_pub(scan_ip(get_ip(default_values.AWS_PUBLIC_IP)))
    print("%s.............. End of scanning Public IP ..............")%br
    print " "

def run_port_checker():
    scan_local_ip()
    #scan_private_ip()
    #scan_public_ip()
    

