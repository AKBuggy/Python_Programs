import socket
import threading
import os

# Define a function to handle each client's requests
def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")

    # Receive the file name from the client
    file_name = client_socket.recv(1024).decode()
    print(f"Client requested file: {file_name}")

    # Check if the file exists
    if os.path.exists(file_name):
        # Open the file and send its contents to the client
        with open(file_name, 'rb') as file:
            data = file.read()
            client_socket.sendall(data)
        print("File sent successfully")
    else:
        # If the file does not exist, inform the client
        error_msg = "File not found"
        client_socket.sendall(error_msg.encode())
        print("File not found")

    # Close the client socket
    client_socket.close()
    print(f"Connection with {address} closed")

# Define the main function for the server
def main():
    # Define the host and port for the server
    host = '0.0.0.0'  # Listen on all available interfaces
    port = 9999

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        # Accept a new connection
        client_socket, address = server_socket.accept()

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

# Entry point of the program
if __name__ == "__main__":
    main()
