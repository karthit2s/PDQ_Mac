#!/usr/bin/python

import locale
from dialog import Dialog
import subprocess
import tempfile
import sys
import os
import psutil
import pwd
import time
import shutil
import hashlib
import stat
import colorama
import argparse
import re
import requests
import parser
import ftplib
import socket
import fcntl
import struct
import shlex
from sys import exit
import base64
import getpass




menu = raw_input ("Assigning Mac address:\n"

    "wired_pdq_mac() 1\n"
    "wireles_pdq_mac() 2\n"
    "Both 3\n")

if menu == str("1"):
    savinginfile = raw_input ("Wired or Wirless PDQ ")
   (
elimf enu == str("2"):
    print (" wireles_pdq_mac2")
#elif menu == str("3"):
 #   print ("Both 3")


def wired_pdq_mac():
    textToSearch = 'PAX Computer Technology'
   # terminal_rows, terminal_cols = d.maxsize()
    pdq_mac_address=$(sudo arp-scan -l | grep '00\|54\|88' | awk '{ print $2 }');
    #code, pdq_mac_address = d.inputbox("Enter the Mac address for Wired PDQ.",
    #    height=max(terminal_rows - 10, 15),
     #   width=max(terminal_cols - 16, 54))
    if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", pdq_mac_address.lower()):
        create_fusion_descovery_script()
        with open('/home/client/fusion-linux/fusion_discover.py', 'r') as file :
            filedata = file.read()
            filedata = filedata.replace(textToSearch, pdq_mac_address)
        with open('/home/client/fusion-linux/fusion_discover.py', 'w') as file:
            file.write(filedata)
        os.system("chmod +x /home/client/fusion-linux/fusion_discover.py")
        os.system("chown client:client /home/client/fusion-linux/fusion_discover.py")
    else:
        print("Invalid Mac Address")

def wireles_pdq_mac():
    create_fusion_descovery_script()

    textToSearch = 'Redpine Signals, Inc.'
#    terminal_rows, terminal_cols = d.maxsize()
#    code, pdq_mac_address = d.inputbox("Enter the Mac address for Wireless PDQ.",
#       height=max(terminal_rows - 10, 15),
#      width=max(terminal_cols - 16, 54))
    pdq_mac_address=$(sudo arp-scan -l | grep '00\|54\|88' | awk '{ print $2 }')
    if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", pdq_mac_address.lower()):
        with open('/home/client/fusion-linux/fusion_discover.py', 'r') as file :
            filedata = file.read()
            filedata = filedata.replace(textToSearch, pdq_mac_address)
        with open('/home/client/fusion-linux/fusion_discover.py', 'w') as file:
            file.write(filedata)
        os.system("chmod +x /home/client/fusion-linux/fusion_discover.py")
        os.system("chown client:client /home/client/fusion-linux/fusion_discover.py")
    else:
        print("invalid Mac Address")


#d =Dialog(dialog="dialog")

