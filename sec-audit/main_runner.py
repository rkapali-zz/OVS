
from plugins import jail_check
from plugins import ossec_ids_check
from plugins import aws_port_check
from plugins import packages_check
from plugins import os_check
from plugins import postfix_check
from plugins import modsecurity_check
from plugins import default_values
from plugins import db_check
import pdfkit
import glob, os

 
boldstart = default_values.BOLDSTART 
boldend = default_values.BOLDEND
itastart = default_values.ITALICSTART 
itaend = default_values.ITALICEND  
h3start = default_values.H3START 
h3end = default_values.H3END  
br = default_values.BR

print "Server Grade : B"
print " "
print "%s**************Awesome name not decided TOOL's report*************************%s %s" %(h3start,h3end,br)
print " "
print " %s*************** Checking OS ***************%s %s" %(boldstart,boldend,br)
try:
	os_check.run_os_checker()
	print " %s%s*************** END of OS Check ***************%s %s %s" %(br,boldstart,boldend,br,br)
except Exception as e:
	print e

print " "
print " %s%s*************** Checking PHP modules ***************%s" %(br,boldstart,boldend)
try:
	packages_check.run_packages_checker()
	print " %s%s*************** END of the PHP modules check ***************%s %s %s" %(br,boldstart,boldend,br,br)
except:
	pass

print " "
print " %s*************** Checking ports ***************%s %s" %(boldstart,boldend,br)
try:
	print "Skipped%s"%br
	#aws_port_check.run_port_checker()
	print " %s%s*************** END of the Port Scanning ***************%s %s %s" %(br,boldstart,boldend,br,br)
except:
	pass

# print " "
# print " %s%s*************** Checking Fail2ban ***************%s %s" %(br,boldstart,boldend,br)
# try:
# 	#print "Skipped%s"%br
# 	jail_check.run_jail_checker()
# 	print " %s%s*************** END of the Fail2ban check ***************%s %s %s" %(br,boldstart,boldend,br,br)
# except:
# 	pass

# print " "
# print " %s%s*************** Checking postfix ***************%s %s" %(br,boldstart,boldend,br)
# try:
# 	#print "Skipped%s"%br
# 	postfix_check.run_postfix_checker()
# 	print " %s%s*************** END of the Postfix check ***************%s %s %s" %(br,boldstart,boldend,br,br)
# except:
# 	pass

print " "
print " %s%s*************** Checking IDS (OSSEC) ***************%s" %(br,boldstart,boldend)
try:
	ossec_ids_check.run_ids_checker()
	print " %s%s*************** END of the IDS check ***************%s %s %s" %(br,boldstart,boldend,br,br)
except:
	pass

print " "
print " %s%s*************** Checking WAF (Modsecurity) ***************%s" %(br,boldstart,boldend)
try:
	modsecurity_check.run_modsecurity_checker()
	print " %s%s*************** END of the ModSecurity check ***************%s %s %s" %(br,boldstart,boldend,br,br)
except :
	pass 
	
print " "
print " %s%s*************** Checking DB (MySQL) ***************%s" %(br,boldstart,boldend)
try:
	db_check.run_db_checker()
	print " %s%s*************** END of the ModSecurity check ***************%s %s %s" %(br,boldstart,boldend,br,br)
except Exception as e:
	print e

print " "
print "%s**************End of Testing*************************%s %s" %(h3start,h3end,br)

for file in glob.glob("*.html"):
	pdfkit.from_file(file, '%s.pdf'%file)
