import socket

# Define the server address and port
server_address = '127.0.0.1'  # Replace with the actual server IP address
server_port = 9999

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_address, server_port))
print(f"Connected to {server_address}:{server_port}")

# Ask the user for the file name to download
file_name = input("Enter the file name you want to download: ")

# Send the file name to the server
client_socket.sendall(file_name.encode())

# Receive the file contents from the server
data = client_socket.recv(1024)

# Check if the file exists
if data.decode() == "File not found":
    print("File not found on server.")
else:
    # Save the received data to a file
    with open(file_name, 'wb') as file:
        file.write(data)
    print(f"File '{file_name}' downloaded successfully.")

# Close the socket
client_socket.close()
