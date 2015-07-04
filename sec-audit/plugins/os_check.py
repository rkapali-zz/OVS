
import subprocess
import default_values
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



## check OS description
def check_os_description():
    banner = " ***************checking OS *************** "

    try:
        p1 = subprocess.Popen("lsb_release -d", stdout=subprocess.PIPE, shell=True)
        (os_output, err) = p1.communicate()
        l_os_output_ = os_output.strip().split(":")
        osdesc = l_os_output_[1].strip()
        #osdesc = str(osdesc)
        #print "here", l_os_output_[1]

    except OSError as oserror:
        print "Error has occured in " +  + p1 + " " + oserror
        exit(200)

    else:
        if osdesc in default_values.OS_DESCRIPTION: # if os_description match
            print "%sThe OS is <b>%s</b> %s %s"%(okstart,osdesc, ok, okend)
        else:
            print "%sThe OS found to be <b>%s</b> %s %s"%(wrstart,osdesc,warning,wrend)
            print " %s" %default_values.OSRECOM
            


    ## check OS bit
    try:
        p4 = subprocess.Popen("uname -i", stdout=subprocess.PIPE, shell=True)
        (os_bit_output, err) = p4.communicate()


    except OSError as osbiterror:
        print "Error has occured in " + p4 + " " + osbiterror
        exit(200)

    else:
        if default_values.OS_BIT== os_bit_output.strip() :                              # if os_description match
            print "%s%sThe OS is <b>%s</b> bit %s %s"%(br,okstart,default_values.OS_BIT,ok,okend)
        else:
            print "%s%sThe OS found to be of <b>%s</b> %s %s" %(br,wrstart,os_bit_output,warning,wrend)
            print " %s" %default_values.OSRECOM
            r_osbitOutput = "The OS found to be of " + os_bit_output + warning

    #print "******** End of Checking OS version and bit ********"




def run_os_checker():
    check_os_description()
    # txtReport.create_txt_file()

#run_osChecker()
