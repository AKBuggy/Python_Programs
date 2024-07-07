import telnetlib
import threading


# Function to receive messages from the server
def receive_messages():
    while True:
        response = tn.read_until(b"\n").decode()  # Read until newline character
        print(response, end="")


# Server configuration
HOST = "127.0.0.1"
PORT = 55555

# Connect to the server
tn = telnetlib.Telnet(HOST, PORT)

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

try:
    while True:
        message = input("Enter message: ")
        tn.write(message.encode() + b"\n")
except KeyboardInterrupt:
    tn.close()
