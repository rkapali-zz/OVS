__author__ = 'sabin'


__author__ = 'sabin'

import ConfigParser


def load_config(config_file):
    conf = ConfigParser.ConfigParser()
    conf.read (config_file)
    conf._sections

    config_info = {}
    config_info['php5-mysql'] = conf.get('pkg', 'php5-mysql')
    config_info['php5-mcrypt'] = conf.get('pkg', 'php5-mcrypt')
    config_info['php5-curl'] = conf.get('pkg', 'php5-curl')
    config_info['php5-gd'] = conf.get('pkg', 'php5-gd')
    config_info['php5-common'] = conf.get('pkg', 'php5-common')
    config_info['libapache2-mod-php5'] = conf.get('pkg', 'libapache2-mod-php5')
    config_info['apache2'] = conf.get('pkg', 'apache2')
    config_info['libapache2-modsecurity']  = conf.get('pkg', 'libapache2-modsecurity')
    config_info['php5-curl'] = conf.get('pkg', 'php5-curl')

    #print config_info
    for k, v in config_info.items():
        pass
        #print " loops ", k, " ", v
    return config_info


#conf = load_config('standards.conf')

if __name__ == '__main__':
    load_config('serverAuditor.conf')