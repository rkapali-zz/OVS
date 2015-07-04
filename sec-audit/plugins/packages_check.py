
__author__ = 'Sabin'


import apt
from conf_loader import module_conf


ok = " .......................................[OK]"
warning = " .......................................[WARNING]"
not_installed = " .......................................[NOT INSTALLED]"
load_conf = module_conf.load_config('templates/serverAuditor.conf')
cache = apt.cache.Cache()

def check_packages(package_name, package_version):
    print "............................................................................."
    print 'Checking for ', package_name, " version ", package_version

    package = cache[package_name]
    name = package.shortname

    # check if package is installed in the server
    if package.is_installed:
        installed_version = package.installed
        installed_version = str(installed_version)
        installed_version = installed_version.split()
        installed_version = installed_version[2][9:-2]
        if installed_version == package_version:
            print "%s with %s installed %s" %(name,installed_version,ok)
        else:
            print "%s, expecting version %s, installed ver %s %s" %(name,package_version,installed_version,warning)
    else:
        print "%s %s" %(name,not_installed)

def run_packages_checker():
    for k,v in load_conf.iteritems():
        check_packages(k, v)
