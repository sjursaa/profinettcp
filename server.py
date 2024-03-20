import socket

# Server configuration
SERVER_HOST = '127.0.0.1'  # localhost
SERVER_PORT = 12345

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Listen for incoming connections
server_socket.listen()

print(f"[*] Listening on {SERVER_HOST}:{SERVER_PORT}")

while True:
    # Accept a new connection
    client_socket, client_address = server_socket.accept()
    print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

    # Handle the connection
    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break  # No more data, connection closed by the client
            print(f"Received data from {client_address[0]}:{client_address[1]}: {data.decode()}")

            # Echo the data back to the client
            client_socket.sendall(data)
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the client socket
        client_socket.close()
        print(f"[*] Connection with {client_address[0]}:{client_address[1]} closed")

# Close the server socket (this won't be reached in this example)
server_socket.close()

