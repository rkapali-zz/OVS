
import default_values
from conf_loader import modsecurity_conf
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


# ok = " .......................................[OK]"
# warning = " .......................................[WARNING]"
# error = " .......................................[NOT INSTALLED]"

## checking modsecurity settings. This method should be called only if modsecurity is installed in the system.
def check_modsecurity():
    status_engine = ""
    ruleEngine = ""
    response_body_access = ""
    audit_log = ""

    try:
        status_engine = modsecurity_conf.load_conf(default_values.MODSECURITY_CONF_lOCATION).get("SecStatusEngine")
        ruleEngine = modsecurity_conf.load_conf(default_values.MODSECURITY_CONF_lOCATION).get("SecRuleEngine")
        response_body_access = modsecurity_conf.load_conf(default_values.MODSECURITY_CONF_lOCATION).get("SecResponseBodyAccess")
        audit_log = modsecurity_conf.load_conf(default_values.MODSECURITY_CONF_lOCATION).get("SecAuditLog")
    except:
        status_engine = ""
        ruleEngine = ""
        response_body_access = ""
        audit_log = ""

#print "the value of status  = " + status_engine + " " + ruleEngine + " " + response_body_access + " " + audit_log
    print "%schecking Apache Modsecurity Firewall Settings %s"%(br,br)
    print "Reading /etc/modsecurity/modsecurity.conf %s" %br
    try:
        if status_engine == default_values.MODSECURITY_SEC_STATUS_ENGINE:
            print " %sThe modsecurity engine status is %s %s %s" %(okstart,str(status_engine),ok,okend)
        elif status_engine != "" :
            print " %sThe modsecurity engine status is %s %s %s " %(wrstart,str(status_engine),warning,wrend)

        if ruleEngine == default_values.MODSECURITY_SEC_RULE_ENGINE:
            print " %sThe modsecurity rule engine status is %s %s %s" %(okstart,str(ruleEngine),ok,okend)
        elif ruleEngine != "" :
            print " %sThe modsecurity rule engine status is %s %s %s" %(wrstart,str(ruleEngine),warning,wrend)

        if response_body_access == default_values.MOSECURITY_Sec_RESPONSE_BODY_ACCESS:
            print " %sThe modsecurity response_body_access is %s %s %s" %(okstart,response_body_access,ok,okend)
        elif response_body_access != "" :
            print " %sThe modsecurity response_body_access is %s %s This setting might consume more server memory %s" %(wrstart,response_body_access,warning,wrend)
        
        if status_engine != "":                                                                          
            print " The location of the modsecurity audit log is " + audit_log
        
        if status_engine == "" or ruleEngine == "" or response_body_access == "" or audit_log == "" :
            print "%sModsecurity %s %s" %(erstart,error,erend)
        print " "
        #print " End of Testing Modsecurity settings. Please do the Needful %s"%br
    except IOError as checkModsecurityError:
        print (" Error has occur in " + "checkModsecurity()" + " " + checkModsecurityError.strerror)


def run_modsecurity_checker():
    check_modsecurity()
