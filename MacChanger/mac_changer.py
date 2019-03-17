#!/usr/bin/env python

import subprocess

interface = "wlan0"
new_mac = "00:11:33:55:77:99"



subprocess.call("ifconfig" + interface + "down", Shell=True)
subprocess.call("ifconfig" + interface + "hw ether 00:11:22:33:44:55", Shell=True)
subprocess.call("ifconfig" + interface + "up", Shell=True)

