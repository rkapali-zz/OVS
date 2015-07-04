

import apt
from conf_loader import module_conf
import default_values

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

#ok = " .......................................[OK]"
#warning = " .......................................[WARNING]"
#not_installed = " .......................................[NOT INSTALLED]"
load_conf = module_conf.load_config('templates/serverAuditor.conf')
cache = apt.cache.Cache()

def check_packages(package_name, package_version):
    #print "%s ............................................................................."%br
    print "%s Checking for %s%s%s version %s%s%s"%(br,okstart,package_name,okend,okstart,package_version,okend)

    package = cache[package_name]
    name = package.shortname

    # check if package is installed in the server
    if package.is_installed:
        installed_version = package.installed
        installed_version = str(installed_version)
        installed_version = installed_version.split()
        installed_version = installed_version[2][9:-2]
        if installed_version == package_version:
            print "Installed version %s </b>%s</b> %s %s" %(okstart,installed_version,ok,okend)
        else:
            #print "%s <b><i>%s</i></b>; standard version <b><i>%s</i></b>; installed version <b>%s</b> %s %s" %(wrstart,name,package_version,installed_version,warning,wrend)
            print "Installed version %s <b>%s</b> %s %s" %(wrstart,installed_version,warning,wrend)
            print " %s" %default_values.PHPRECOM
    else:
        print "%s <b><i>%s</i></b> %s %s" %(erstart,name,error,erend)
        print " %s" %default_values.PHPRECOM

def run_packages_checker():
    for k,v in load_conf.iteritems():
        check_packages(k, v)
