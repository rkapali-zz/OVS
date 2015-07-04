__author__ = 'sabin'

import subprocess
import default_values
from conf_loader.server_auditor_conf import conf


ok = " .......................................[OK]"
warning = " .......................................[WARNING]"

## check OS description
def check_os_description():
    banner = " ***************checking OS *************** "

    try:
        p1 = subprocess.Popen("lsb_release -d", stdout=subprocess.PIPE, shell=True)
        (os_output, err) = p1.communicate()
        l_os_output_ = os_output.strip().split(":")
        osdesc = l_os_output_[1].strip()
        #print "here", l_os_output_[1]

    except OSError as oserror:
        print "Error has occured in " +  + p1 + " " + oserror
        exit(200)

    else:

        if default_values.OS_DESCRIPTION == osdesc :                              # if os_description match
            print "The OS is " + osdesc + ok

        else:
            print "The OS found to be: " + osdesc + warning


    ## check OS bit
    try:
        p4 = subprocess.Popen("uname -i", stdout=subprocess.PIPE, shell=True)
        (os_bit_output, err) = p4.communicate()


    except OSError as osbiterror:
        print "Error has occured in " + p4 + " " + osbiterror
        exit(200)

    else:
        if default_values.OS_BIT== os_bit_output.strip() :                              # if os_description match
            print "The OS is " + default_values.OS_BIT + " bit" +ok
        else:
            print "The OS found to be of " + os_bit_output + warning
            r_osbitOutput = "The OS found to be of " + os_bit_output + warning


    print "******** End of Checking OS version and bit ********"




def run_os_checker():
    check_os_description()
    # txtReport.create_txt_file()

#run_osChecker()