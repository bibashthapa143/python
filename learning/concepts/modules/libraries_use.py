import os

# listing diles in a directory
print(os.listdir())

import subprocess
result = subprocess.run(["ls","-la"], capture_output=True, text=True)
print(result.stdout)

'''
List of popular libraries:
OS
Subprocess
Socket
Scapy
Cryptography
Requests
Paramiko
python-nmap
Pyshark
Impacket
'''
