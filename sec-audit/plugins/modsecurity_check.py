__author__ = 'sabin'

import default_values
from conf_loader import modsecurity_conf
from conf_loader.server_auditor_conf import conf

# different standards in variables

ok = " .......................................[OK]"
warning = " .......................................[WARNING]"

## checking modsecurity settings. This method should be called only if modsecurity is installed in the system.
def check_modsecurity():

    status_engine = modsecurity_conf.load_conf(default_values.MODSECURITY_CONF_lOCATION).get("SecStatusEngine")
    ruleEngine = modsecurity_conf.load_conf(default_values.MODSECURITY_CONF_lOCATION).get("SecRuleEngine")
    response_body_access = modsecurity_conf.load_conf(default_values.MODSECURITY_CONF_lOCATION).get("SecResponseBodyAccess")
    audit_log = modsecurity_conf.load_conf(default_values.MODSECURITY_CONF_lOCATION).get("SecAuditLog")

#print "the value of status  = " + status_engine + " " + ruleEngine + " " + response_body_access + " " + audit_log
    print "checking Apache Modsecurity Firewall Settings "
    print "Reading /etc/modsecurity/modsecurity.conf "
    try:
        if status_engine == default_values.MODSECURITY_SEC_STATUS_ENGINE:
            print " The modsecurity engine status is " + str(status_engine) + ok
        else:
            print " The modsecurity engine status is " + str(status_engine) + warning

        if ruleEngine == default_values.MODSECURITY_SEC_RULE_ENGINE:
            print " The modsecurity rule engine status is " + str(ruleEngine) + ok
        else:
            print " The modsecurity rule engine status is " + str(ruleEngine) + warning

        if response_body_access == default_values.MOSECURITY_Sec_RESPONSE_BODY_ACCESS:
            print " The modsecurity response_body_access is " + response_body_access + ok
        else:
            print " The modsecurity response_body_access is " + response_body_access + " This setting might consume more server" \
                                                                                  " memory" + warning
        print " The location of the modsecurity audit log is " + audit_log
        print " "
        print " End of Testing Modsecurity settings. Please do the Needful"
    except IOError as checkModsecurityError:
        print (" Error has occur in " + "checkModsecurity()" + " " + checkModsecurityError.strerror)


def run_modsecurity_checker():
    check_modsecurity()
