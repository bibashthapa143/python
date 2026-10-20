# classify_ports.py

services = {22: "ssh", 80: "http", 443: "https"}  # port: service name

def classify(ports):
    result = {}
    for port in ports:                 # check each port
        result[port] = services.get(port, "UNKNOWN") # "unknown" if not found
    return result                      # after the loop

if __name__ == "__main__":             # run only when file is run directly
   while True:
    user_input = input("Enter ports: ")

    try:
       ports = [int(p) for p in user_input.split(",")]
    except ValueError:
       print("Invalid input")
       continue


    
    

   
    for port, service in classify(ports).items():   # port and service together
        print(f"{port} -> {service}")
