__author__ = 'sabin'


# This module consist of some default values that will be used in script as constant for that version of script

# OS info
OS_DESCRIPTION = "Ubuntu 14.04.1 LTS"
OS_BIT= "x86_64"

# Ossec HIDS
OSSEC_INIT_CONF = "/etc/ossec-init.conf"
OSSEC_VERSION = "v2.8"

### standard modsecurity settings
MODSECURITY_SEC_STATUS_ENGINE = "On"
MODSECURITY_SEC_RULE_ENGINE = "On"
MOSECURITY_Sec_RESPONSE_BODY_ACCESS = "Off"
MODSECURITY_CONF_lOCATION = "/etc/modsecurity/modsecurity.conf"

# different standards for the postfix
POSTFIX_MAIN_LOCATION = "/etc/postfix/main.cf"
POSTFIX_MY_NETWORK = "127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128"
POSTFIX_SMTPD_USE_TLS = "yes"

# AWS IP
AWS_LOCAL_IP = "127.0.0.1"
AWS_PUBLIC_IP = "http://169.254.169.254/latest/meta-data/public-ipv4/"
AWS_PRIVATE_IP = "http://169.254.169.254/latest/meta-data/local-ipv4"

# Fail2ban info
JAIL_CONF_LOCATION  = "/etc/fail2ban/jail.conf"
JAIL_LOCAL_LOCATION = "/etc/fail2ban/jail.local"
