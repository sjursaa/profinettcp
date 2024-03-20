import socket

# Profinet server address and port
PROFINET_SERVER_ADDRESS = 'localhost' # change dis bish
PROFINET_SERVER_PORT = 12345 # change dis bish

"""
03 00 00 44 02 f0 80 header
data 

"""

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the Profinet server
    client_socket.connect((PROFINET_SERVER_ADDRESS, PROFINET_SERVER_PORT))
    
    # Send data to the server
    message = b'Hello, Profinet Server!'
    client_socket.sendall(message)

    # Receive response from the server
    response = client_socket.recv(1024)
    print('Received:', response.decode())
    hex_representation = ' '.join([hex(response) for response in response])
    print(hex_representation)

except Exception as e:
    print('An error occurred:', e)

finally:
    # Close the socket
    client_socket.close()

