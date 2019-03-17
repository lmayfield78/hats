#!/usr/bin/env python

import subprocess

interface = "wlan0"
new_mac = "00:11:33:55:77:99"



subprocess.call("ifconfig" + interface + "down", shell=True)
subprocess.call("ifconfig" + interface + "hw ether" + new_mac, shell=True)
subprocess.call("ifconfig" + interface + "up", shell=True)

