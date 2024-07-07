import socket
import threading
import os


# Function to handle each client connection
def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")

    # Receive the file name
    file_name = client_socket.recv(1024).decode()
    print(f"Receiving file: {file_name}")

    # Open a new file to save the received data
    with open(file_name, "wb") as f:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            f.write(data)

    print(f"File {file_name} received successfully")

    # Close the client socket
    client_socket.close()


# Main function to start the server
def main():
    # Host and port to listen on
    host = "0.0.0.0"
    port = 8888

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Start listening for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    try:
        while True:
            # Accept incoming connections
            client_socket, address = server_socket.accept()

            # Create a new thread to handle the connection
            client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server stopped.")

    # Close the server socket
    server_socket.close()


if __name__ == "__main__":
    main()
