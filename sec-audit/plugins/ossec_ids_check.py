
import os
import subprocess
import default_values
from conf_loader import ossec_init
from third_party import xmltodict

from conf_loader.server_auditor_conf import conf

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

ok = " .......................................[OK]"
warning = " .......................................[WARNING]"
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
    print ("Checking system for presence of OSSEC HIDS and its state")
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
                print ("  OSSEC HIDS version is ") + check_ids_version() + "......................" + ok
            else:
                print("  OSSEC HIDS version installed is ") + check_ids_version() + "......................" + warning

            if check_ids_type() == ossec_type_server:
                print ("  OSSEC HIDS Type " + ossec_type_server + ok)
                email_notification_status = xmltodict.parse(read_ossec_conf)['ossec_config']['global']['email_notification'] # should be yes
                email_notification_to = xmltodict.parse(read_ossec_conf)['ossec_config']['global']['email_to']           # should be equal to ossec_mail_alert_id
                active_response_status = xmltodict.parse(read_ossec_conf)['ossec_config']['active-response']['disabled']   # should be no

                    # conditioning for ossec server
                if email_notification_status =='yes':
                    print ("  OSSEC HIDS Email Notification is Activated") + "......................" + ok
                    if email_notification_to == ossec_mail_alert_id:
                        print ("OSSEC HIDS Email is ") + email_notification_to + "......................" + ok
                    else:
                        print ("OSSEC HIDS Email is ") + email_notification_to + "......................" + warning

                else:
                    print ("OSSEC HIDS Email Notification is NOT Activated") + "......................" + warning

                if active_response_status =='yes':
                    print ("OSSEC HIDS Active Response status is ") + active_response_status + "......................" + ok

                else:
                    print ("OSSEC HIDS Active Response status is ") + active_response_status + "......................" + warning

            elif(check_ids_type() == ossec_type_agent):
                    print ("  OSSEC HIDS Type ") + ossec_type_agent + ok
                    ossec_server_ip = xmltodict.parse(read_ossec_conf)['ossec_config']['client']['server-ip']

                    # conditioning for ossec agent
                    if ossec_server_ip == ossec_central_server_ip:
                        print (" OSSEC HIDS Central Server IP is ") + ossec_server_ip + "......................" + ok
                    else:
                        print (" OSSEC HIDS Central Server IP is ") + ossec_server_ip + "......................" + warning
            else:
                print ("  OSSEC HIDS Type is UNKNOWN and not according to standard ") + "......................" + warning

            # checking if ossec is running
            try:
                ossec_syscheck = subprocess.Popen("./var/ossec/bin/ossec-syscheckd", stdout=subprocess.PIPE, shell=True)
                (ossec_syscheck_output, err) = ossec_syscheck.communicate()

                filter_ossec_syscheck_output = ossec_syscheck_output.find(ossec_error)

            except IOError as ossecioerror:
                print ("Error occured in " + "checkIds()") + " " + ossecioerror.strerror

            else:
                if filter_ossec_syscheck_output >= 0:
                    print (" " + " OSSEC HIDS is not Running State " + warning)
                else:
                    print (" OSSEC HIDS is in Running State ") + "......................" + ok

        else:
            print (" Could not find OSSEC HIDS in the System ") + "......................" + warning

    except IOError as checkIdsError:
        print (" Error has occur in " + "checkIds()" + " " + checkIdsError.strerror)

def run_ids_checker():
    check_hids()

## calling all functions
#run_idsChecker()

