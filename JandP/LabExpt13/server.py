import socket
import threading

# Global variables
HOST = '127.0.0.1'  # Localhost
PORT = 55555  # Port to listen on
clients = []  # List to store client connections


def handle_client(client_socket):
    while True:
        try:
            # Receive message from client
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            print(f"Received: {message}")

            # Broadcast message to all clients
            broadcast(message, client_socket)
        except Exception as e:
            print(f"Error: {e}")
            break

    # Remove client from list and close connection
    clients.remove(client_socket)
    client_socket.close()


def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Error broadcasting message: {e}")
                client.close()
                clients.remove(client)


def main():
    # Create socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket to address and port
    server_socket.bind((HOST, PORT))

    # Listen for incoming connections
    server_socket.listen(5)
    print(f"[*] Listening on {HOST}:{PORT}")

    while True:
        try:
            # Accept connection from client
            client_socket, addr = server_socket.accept()
            print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

            # Add client to list
            clients.append(client_socket)

            # Create a new thread to handle client communication
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
        except KeyboardInterrupt:
            print("[*] Server shutting down...")
            break

    # Close server socket
    server_socket.close()


if __name__ == "__main__":
    main()
