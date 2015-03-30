# setpurplestatus
Set the correct pidgin status message, depending on network connection

## Installation
You need to install the following dependencies:
 * pyYAML
 * python-netifaces
 * python-netaddr

## Configuration
Create a ~/.setpurplestatusrc to configure networks and status messages.

### Example
    interfaces:
        - 'eth0'
        - 'wlan0'
    networks:
        '192.168.0.0/24':
            status: 'at home'
        '10.0.0.0/16':
            status: 'at work