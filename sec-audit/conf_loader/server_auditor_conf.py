__author__ = 'sabin'

import ConfigParser
import os
from report import txt_report

def load_config(config_file):
    try:
        conf = ConfigParser.ConfigParser()
        conf.read (config_file)

        config_info = {}

        config_info['ossec-ids.ossec_type_agent'] = conf.get('ossec-ids', 'ossec_type_agent')
        config_info['ossec-ids.ossec_type_server'] = conf.get('ossec-ids', 'ossec_type_server')
        config_info['ossec-ids.ossec_error'] = conf.get('ossec-ids', 'ossec_error')
        config_info['ossec-ids.ossec_mail_alert_id'] = conf.get('ossec-ids', 'ossec_mail_alert_id')
        config_info['ossec-ids.ossec_central_server_ip'] = conf.get('ossec-ids', 'ossec_central_server_ip')

        config_info['network.valid_tcp_port_list_lo'] = conf.get('network', 'valid_tcp_port_list_lo')
        config_info['network.valid_tcp_port_list_eth0'] = conf.get('network', 'valid_tcp_port_list_eth0')
        config_info['network.valid_tcp_port_list_pub'] = conf.get('network', 'valid_tcp_port_list_pub')

        config_info['fail2ban.ssh_ignoreip_list'] = conf.get('fail2ban', 'ssh_ignoreip_list')
        config_info['fail2ban.ssh_enabled'] = conf.get('fail2ban', 'ssh_enabled')

        config_info['fail2ban.ssh_port'] = conf.get('fail2ban', 'ssh_port')
        config_info['fail2ban.ssh_filter'] = conf.get('fail2ban', 'ssh_filter')
        config_info['fail2ban.ssh_logpath'] = conf.get('fail2ban', 'ssh_logpath')
        config_info['fail2ban.ssh_maxretry'] = conf.get('fail2ban', 'ssh_maxretry')
        config_info['fail2ban.ssh_bantime'] = conf.get('fail2ban', 'ssh_bantime')
        config_info['fail2ban.ssh_findtime'] = conf.get('fail2ban', 'ssh_findtime')

        return config_info

    except IOError as server_auditor_confLoader:
        print (" Error has occur in " + "load_config()" + " " + server_auditor_confLoader.strerror)

if os.path.exists("templates/serverAuditor.conf"):

    file_exist = "server_auditor.conf file exist. yee!!!"
    print file_exist
    print "Generating Report in .txt Format"
    conf = load_config('templates/serverAuditor.conf')
    txt_report.create_txt_file()

else:
    print " ERROR: Main Standard configuration File ('server_auditor.conf') " + "is Missing."
