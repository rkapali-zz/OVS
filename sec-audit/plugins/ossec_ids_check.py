import os
import subprocess
import default_values
from conf_loader import ossec_init
from third_party import xmltodict

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
rastart = default_values.RASTART
raend = default_values.RAEND 
br = default_values.BR

#conf = serverAuditor_confLoader.load_config('serverAuditor.conf')

## ossec standards
# ossec_init_conf = conf.get("ossec-ids.ossec_init_conf")
# ossec_version = conf.get("ossec-ids.ossec_version")
ossec_type_agent = conf.get("ossec-ids.ossec_type_agent")
ossec_type_server = conf.get("ossec-ids.ossec_type_server")
ossec_error = conf.get("ossec-ids.ossec_error")
ossec_mail_alert_id = conf.get("ossec-ids.ossec_mail_alert_id")
ossec_central_server_ip = conf.get("ossec-ids.ossec_central_server_ip")
## end of ossec standards

# ok = " .......................................[OK]"
# warning = " .......................................[WARNING]"
# error = " .......................................[NOT INSTALLED]"

#ossec_init_conf = "test_ossec-init.txt"

# loading the ids_confLoader and getting the ids_type and ids_version from the /etc/ossec-init.conf
def check_ids_type():

    ids_type = ossec_init.load_conf(default_values.OSSEC_INIT_CONF).get('TYPE')
    ids_type = ids_type[1:-1]
    print ("checking ids_type value " + ids_type)
    return ids_type

def check_ids_version():

    ids_version = ossec_init.load_conf(default_values.OSSEC_INIT_CONF).get('VERSION')
    ids_version = ids_version[1:-1]
    print ("checking ids_version value " + ids_version)
    return ids_version

def check_ids_directory():
    ids_directory = ossec_init.load_conf(default_values.OSSEC_INIT_CONF).get('DIRECTORY')
    ids_directory = ids_directory[1:-1] # removing double quotes from the string

    ossec_conf_sub = "/etc/ossec.conf"
    ossec_conf = ids_directory + ossec_conf_sub
    print (" checking ossec.conf "+ ossec_conf)
    return ossec_conf

#### Checking system for presence of OSSEC HIDS and its state
def check_hids():
    print ("%s Checking system for presence of OSSEC HIDS and its state%s")%(br,br)
    #ossec_folderpath = "/var/ossec"
    #ossec_conf = ids_directory + "/etc/ossec.conf"

    #checking system for installed OSSEC HIDS
    try:
        if os.path.exists(default_values.OSSEC_INIT_CONF):
            print (" OSSEC HIDS is Installed. Checking Further Settings...")

            # opening and reading ossec-init.conf file for versioning and type info
            print ("opening and reading ossec-init.conf file for versioning and type info")

            open_ossec_init_conf_file = open(default_values.OSSEC_INIT_CONF)
            print ("reading ossec_init_conf")

            #read_ossec_init_conf_file = open_ossec_init_conf_file.read()
            #opening, reading and parsing ossec.conf file for checking email, server, active response, etc

            open_ossec_conf = open(check_ids_directory())
            read_ossec_conf = open_ossec_conf.read()

            #checking ossec version
            #search_ossec_version = read_ossec_init_conf_file.find(os_version)
            if check_ids_version() == default_values.OSSEC_VERSION:
                print (" %s OSSEC HIDS version is  %s %s %s ")%(okstart,check_ids_version(),ok,okend)
            else:
                print(" %s OSSEC HIDS version installed is %s %s %s")%(wrstart,check_ids_version(),warning,wrend)

            if check_ids_type() == ossec_type_server:
                print (" %s OSSEC HIDS Type %s %s %s")%(okstart,ossec_type_server,ok,okend)
                email_notification_status = xmltodict.parse(read_ossec_conf)['ossec_config']['global']['email_notification'] # should be yes
                email_notification_to = xmltodict.parse(read_ossec_conf)['ossec_config']['global']['email_to']           # should be equal to ossec_mail_alert_id
                active_response_status = xmltodict.parse(read_ossec_conf)['ossec_config']['active-response']['disabled']   # should be no

                    # conditioning for ossec server
                if email_notification_status =='yes':
                    print (" %s OSSEC HIDS Email Notification is Activated %s %s")%(okstart,ok,okend)
                    if email_notification_to == ossec_mail_alert_id:
                        print ("%sOSSEC HIDS Email is %s %s %s")%(okstart,email_notification_to,ok,okend)
                    else:
                        print ("%sOSSEC HIDS Email is %s %s %s") %(wrstart,email_notification_to,warning,wrend)

                else:
                    print ("%s OSSEC HIDS Email Notification is NOT Activated %s %s")%(wrstart,warning,wrend)

                if active_response_status =='yes':
                    print ("%sOSSEC HIDS Active Response status is %s %s %s") %(okstart,active_response_status,ok,okend)

                else:
                    print ("%sOSSEC HIDS Active Response status is %s %s %s") %(wrstart,active_response_status,warning,wrend)

            elif(check_ids_type() == ossec_type_agent):
                    print (" %s OSSEC HIDS Type %s %s %s") (okstart,ossec_type_agent,ok,okend)
                    ossec_server_ip = xmltodict.parse(read_ossec_conf)['ossec_config']['client']['server-ip']

                    # conditioning for ossec agent
                    if ossec_server_ip == ossec_central_server_ip:
                        print (" %sOSSEC HIDS Central Server IP is %s %s %s") %(okstart,ossec_server_ip,ok,okend)
                    else:
                        print (" %sOSSEC HIDS Central Server IP is %s %s %s") %(wrstart,ossec_server_ip,warning,wrend)
            else:
                print (" %s OSSEC HIDS Type is UNKNOWN and not according to standard %s %s") %(wrstart,warning,wrend)

            # checking if ossec is running
            try:
                ossec_syscheck = subprocess.Popen("./var/ossec/bin/ossec-syscheckd", stdout=subprocess.PIPE, shell=True)
                (ossec_syscheck_output, err) = ossec_syscheck.communicate()

                filter_ossec_syscheck_output = ossec_syscheck_output.find(ossec_error)

            except IOError as ossecioerror:
                print ("Error occured in " + "checkIds()") + " " + ossecioerror.strerror

            else:
                if filter_ossec_syscheck_output >= 0:
                    print (" " + " %sOSSEC HIDS is not Running State %s %s") %(wrstart,warning,wrend)
                else:
                    print (" %sOSSEC HIDS is in Running State %s %s") %(okstart,ok,okend)

        else:
            print (" %sCould not find OSSEC HIDS in the System%s %s") %(erstart,error,erend)

    except IOError as checkIdsError:
        print (" Error has occur in " + "checkIds()" + " " + checkIdsError.strerror)

def run_ids_checker():
    check_hids()

## calling all functions
#run_idsChecker()
