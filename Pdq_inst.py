#!/bin/bash/python

import os

pdq_mac_address=$(sudo arp-scan -l | grep '00\|54\|8c' | awk '{print $2}')


if [[ $pdq_mac_address == tr.startswith'(00)']] then

#if pdq_mac_address == '00':
    
      print("Installiing the Wired PDQ " wired_pdq_mac());
elif
      print("Installing Wireles PDQ" wireles_pdq_mac());
else
      print("Installing both PDQ");



def wired_pdq_mac():
    textToSearch = 'PAX Computer Technology'
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


