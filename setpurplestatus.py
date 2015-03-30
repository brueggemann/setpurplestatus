#!/usr/bin/env python
# purpose: Set the correct pidgin status message, depending on network connection
# copyright: B1 Systems GmbH <info@b1-systems.de>, 2015.
# license: GPLv3+, http://www.gnu.org/licenses/gpl-3.0.html
# author: Jan-Marten Brueggemann <brueggemann@b1-systems.de>, 2015.

import yaml
import netifaces
import os
from netaddr import IPNetwork, IPAddress

CONFIG_PATH = os.getenv('HOME') + '/.setpurplestatusrc'
PURPLEREMOTE = '/usr/bin/purple-remote'

if not os.path.isfile(CONFIG_PATH):
    print("Please create config file in ~/.setpurplestatusrc")
    print("Example:")
    print("interfaces:")
    print("\t- 'eth0'")
    print("\t- 'wlan0'")
    print("networks:")
    print("\t'192.168.0.0/24':")
    print("\t\tstatus: 'at home'")
    print("\t'10.0.0.0/16':")
    print("\t\tstatus: 'at work'")
    exit(2)

stream = open(CONFIG_PATH, 'r')
config = yaml.load(stream)

# Get active network connections
active_interfaces = {}
for interface in config['interfaces']:
    tmpifaddress = netifaces.ifaddresses(interface)
    if 2 in tmpifaddress:
        active_interfaces[interface] = []
        for network in tmpifaddress[2]:
             active_interfaces[interface].append(network['addr'])

# Check matching of configured networks
for network in config['networks']:
    for addresses in active_interfaces.values():
        for address in addresses:
            if IPAddress(address) in IPNetwork(network):
                os.execv(PURPLEREMOTE, [PURPLEREMOTE, 'setstatus?message='+ config['networks'][network]['status']])
                exit(0)
exit(1)
