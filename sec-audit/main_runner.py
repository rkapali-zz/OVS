
from plugins import jail_check
from plugins import ossec_ids_check
from plugins import aws_port_check
from plugins import packages_check
from plugins import os_check
from plugins import postfix_check
from plugins import modsecurity_check


print " "
print " ***************checking OS *************** "
os_check.run_os_checker()

print " "
print " ***************checking Fail2ban *************** "
jail_check.run_jail_checker()

print " "
print " *************** checking modules *************** "
packages_check.run_packages_checker()

print " "
print " *************** checking ports *************** "
aws_port_check.run_port_checker()

print " "
print " *************** checking postfix ***************"
postfix_check.run_postfix_checker()

print " "
print " *************** checking ids (OSSEC) ***************"
ossec_ids_check.run_ids_checker()


print " "
print " *************** checking WAF (Modsecurity) ***************"
modsecurity_check.run_modsecurity_checker()


print " "
print "**************End of Testing*************************"
