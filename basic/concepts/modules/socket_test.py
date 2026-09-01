import socket                                          # load Python's built-in networking module

hostname = socket.gethostname()                        # get this computer's network hostname
print(f"Your computer's hostname: {hostname}")          # display it
