import socket
import os


def send_file(file_path, server_address, server_port):
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((server_address, server_port))

        # Send the file name
        file_name = os.path.basename(file_path)
        client_socket.send(file_name.encode())

        # Open the file and send its contents
        with open(file_path, "rb") as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                client_socket.send(data)

        print(f"File {file_name} sent successfully")
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    finally:
        # Close the socket
        client_socket.close()


if __name__ == "__main__":
    server_address = "127.0.0.1"  # Change this to the IP address of your server
    server_port = 8888  # Change this to the port your server is listening on
    file_path = "./hello.txt"  # Change this to the path of the file you want to send

    send_file(file_path, server_address, server_port)
