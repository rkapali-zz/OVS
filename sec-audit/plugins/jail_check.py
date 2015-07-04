__author__ = 'sabin'

import default_values
import os
from conf_loader.server_auditor_conf import conf
from conf_loader import jail_conf


ok = " .......................................[OK]"
warning = " .......................................[WARNING]"

#conf = serverAuditor_confLoader.load_config('serverAuditor.conf')

#standards of fail2.ban
s_ssh_ignoreip = conf.get("fail2ban.ssh_ignoreip_list")
s_ssh_ignoreip_list = s_ssh_ignoreip.split(',')
s_ssh_enabled = conf.get("fail2ban.ssh_enabled")
s_ssh_port = conf.get("fail2ban.ssh_port")
s_ssh_filter = conf.get("fail2ban.ssh_filter")
s_ssh_logpath = conf.get("fail2ban.ssh_logpath")
s_ssh_maxretry = conf.get("fail2ban.ssh_maxretry")
s_ssh_bantime = conf.get("fail2ban.ssh_bantime")
s_ssh_findtime = conf.get("fail2ban.ssh_findtime")
# end of fail2ban standards

## end of standard

## checking presence of jail.conf or local.conf
def file_presence():
    try:
        if os.path.exists(default_values.JAIL_LOCAL_LOCATION):
            print "Reading /etc/fail2ban/jail.local"
            conf = jail_conf.load_config(default_values.JAIL_LOCAL_LOCATION)
        else:
            print "Reading /etc/fail2ban/jail.conf  Couldn't find file jail.local"
            #conf = jail_confLoader.load_config("sample_jail.conf")
            conf = jail_conf.load_config(default_values.JAIL_CONF_LOCATION)

        return conf
    except IOError as filePresenceError:
        print (" Error has occur in " + "file_presence()" + " " + filePresenceError.strerror)

## checking fail2ban setting from conf file
def check_fail2ban():
    banner = " ***************checking Fail2ban *************** "

    print "Checking Fail2ban Settings....."
    conf=file_presence()
    # getting values from file
    ssh_ignoreip = conf.get("ssh.ignoreip")
    ssh_enabled = conf.get("ssh.enabled")
    ssh_port = conf.get("ssh.port")
    ssh_filter = conf.get("ssh.filter")
    ssh_logpath = conf.get("ssh.logpath")
    ssh_maxretry = conf.get("ssh.maxretry")
    ssh_bantime = conf.get("ssh.bantime")
    ssh_findtime = conf.get("ssh.findtime")

##converting string of ignoreip from conf file into list
    ssh_ignoreip_list = ssh_ignoreip.split(",")
    print " printing the list ", ssh_ignoreip_list
    print " printing our standard ignore ip list ", s_ssh_ignoreip_list


##comparing standard ignore ip list with the list from conf file

    different_ssh_ignoreip = set(s_ssh_ignoreip_list).difference(ssh_ignoreip_list)

    if different_ssh_ignoreip == set():
        print "SSH ignore ip list is ", ssh_ignoreip_list , ok

    else:
        print " SSH ignore ip list mismatched. You missed following IP from standard", different_ssh_ignoreip , warning
        non_standard_ssh_ignoreip = set(ssh_ignoreip_list).difference(s_ssh_ignoreip_list)
        print " SSH ignore ip list mismatched. You having following IP against the standard", non_standard_ssh_ignoreip , warning


    if s_ssh_enabled == str(ssh_enabled):
        print " SSH enable status is ", ssh_enabled , ok


    else:
        print " SSH enable status is ", ssh_enabled , warning


    if s_ssh_port == ssh_port:
        print " SSH port is ", ssh_port , ok

    else:
        print " SSH port is ", ssh_port , warning

    if s_ssh_filter == ssh_filter:
        print " SSH filter is ", ssh_filter , ok

    else:
        print " SSH filter is ", ssh_filter , warning

    if s_ssh_logpath == ssh_logpath:
        print " SSH logpath is ", ssh_logpath , ok

    else:
        print " SSH logpath is ", ssh_logpath , warning


    if s_ssh_maxretry == ssh_maxretry:
        print " SSH maxretry value is ", ssh_maxretry , ok

    else:
        print " SSH maxretry value is ", ssh_maxretry , warning


    if s_ssh_bantime == ssh_bantime:
        print " SSH bantime is ", ssh_bantime , ok

    else:
        print " SSH bantime is ", ssh_bantime , warning


    if s_ssh_findtime == ssh_findtime:
        print " SSH findtime is ", ssh_findtime , ok

    else:
        print " SSH findtime is ", ssh_findtime , warning

def run_jail_checker():
    check_fail2ban()



