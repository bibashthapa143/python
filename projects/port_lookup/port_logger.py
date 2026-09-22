# Dictionary mapping port numbers to their corresponding services
port_services = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS"
}

# Look up the service name for a given port number
def lookup_port(port):
    return port_services.get(port, "Unknown")

# Open the input file for reading and the output file for writing
with open("ports_input.txt", "r") as infile, open("ports_output.txt", "w") as outfile:

    # Process each line in the input file
    for line in infile:
        # Remove leading/trailing whitespace and newline characters
        line = line.strip()

        try:
            # Convert the input text to an integer
            port = int(line)

            # Find the service associated with the port
            service = lookup_port(port)

            # Write the port and service to the output file
            outfile.write(f"{port}: {service}\n")

        except ValueError:
            # Handle entries that are not valid numbers
            outfile.write(f"Skipping invalid entry: {line}\n")

# Display a message when processing is complete
print("Done! Check ports_output.txt")
