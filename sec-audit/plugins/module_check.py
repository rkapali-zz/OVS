
__author__ = 'Sabin'


import apt
from conf_loader import module_conf


ok = " .......................................[OK]"
warning = " .......................................[WARNING]"
load_conf = module_conf.load_config('templates/serverAuditor.conf')
cache = apt.Cache()
installed_packages = cache.keys()


def check_module(module_name, module_version):
    print "............................................................................."
    print 'Checking for ', module_name, " version ", module_version

    # check if package is installed
    if module_name not in installed_packages:
        print "Not installed", warning
    else:
        print "Installed"
    # check if version is correct
        installed_module = cache[module_name]
        keyList1 = list(installed_module.versions.keys())
        print keyList1[0], "--------------------"
        installed_module_version = keyList1[0]
        if installed_module_version != module_version:
            print "Wrong version", warning
        else:
            # version is correct
            print "Installed and right version", ok


def run_module_checker():
    for k,v in load_conf.iteritems():
        check_module (k, v)
