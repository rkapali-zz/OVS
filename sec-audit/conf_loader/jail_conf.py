import ConfigParser


def load_config(config_file):
    try:
        conf = ConfigParser.ConfigParser()
        conf.read (config_file)

        config_info = {}

        config_info['DEFAULT.ignoreip'] = conf.get('DEFAULT', 'ignoreip')
        config_info['DEFAULT.bantime'] = conf.get('DEFAULT', 'bantime')
        config_info['DEFAULT.findtime'] = conf.get('DEFAULT', 'findtime')
        config_info['DEFAULT.maxretry'] = conf.get('DEFAULT', 'maxretry')

        # for ssh
        config_info['ssh.ignoreip'] = conf.get('ssh', 'ignoreip')
        config_info['ssh.enabled'] = conf.get('ssh', 'enabled')
        config_info['ssh.port'] = conf.get('ssh', 'port')
        config_info['ssh.filter'] = conf.get('ssh', 'filter')
        config_info['ssh.action'] = conf.get('ssh', 'action')
        config_info['ssh.logpath'] = conf.get('ssh', 'logpath')
        config_info['ssh.maxretry'] = conf.get('ssh', 'maxretry')
        config_info['ssh.bantime'] = conf.get('ssh', 'bantime')
        config_info['ssh.findtime'] = conf.get('ssh', 'findtime')

        return config_info
    except IOError as jailconfigloader:
        print (" Error has occur in " + "load_config()" + " " + jailconfigloader.strerror)

#conf = load_config('backup.conf.template')
conf = load_config('sample_conf_files/sample_jail.conf')
#print "printing conf ", conf
#print "ssh ignore ip", conf.get("ssh.ignoreip")