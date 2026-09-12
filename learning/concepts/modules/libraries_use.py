import os

# listing diles in a directory
print(os.listdir())

import subprocess
# result = subprocess.run(["ls","-la"], capture_output=True, text=True)
# print(result.stdout)

process = subprocess.Popen(["ping" , "google.com"], stdout=subprocess.PIPE, text=True)

if process.stdout is not None:
    for line in process.stdout:
        print(line.strip())


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
