
# # port_services[443]="HTTPS"   #adds a new entry
# # port_services[80]="HTTP-alt"  #overwrites existing value

# # print(port_services)

# # print(port_services.get(9999))  #prints:None
# # print(port_services.get(9999, "Unknown")) #prints :Unknown

# # port_services[3306]="MySQL"
# # print(port_services.get(3306))
# # print(port_services.get(1111, "not found"))

def lookup_service(port, services_dict):
    return services_dict.get(port,"not found")


#port_services dict
port_services={
    21:"FTP",
    22:"SSH",
    80:"HTTP"
}

#ask user for port number
user_port=int(input("Enter a port number: "))

#call the function and print result
service=lookup_service(user_port, port_services)
print(f"Port {user_port} -> {service}")

print("----------------------------")

user_input = input("Enter ports separated by commas: ")
parts = user_input.split(",")
print(parts)
print(type(parts))

ports = []
for p in parts:
    ports.append(int(p))

print(ports)
print(type(ports[0]))

for port in ports:
    service = lookup_service(port, port_services)
    print(f"Port {port} -> {service}")

port = 22
service = "SSH"
print("Port {port} -> {service}")
print(f"Port {port} -> {service}")

