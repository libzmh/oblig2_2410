import socket
import sys

# Check command-line arguments
if len(sys.argv) != 7 or sys.argv[1] != "-i" or sys.argv[3] != "-p" or sys.argv[5] != "-f":
    print("Usage: python3 client.py -i <server_ip> -p <server_port> -f <filename>")
    sys.exit(1)

server_ip, server_port, file_path = sys.argv[2], int(sys.argv[4]), sys.argv[6]

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((server_ip, server_port))
except:
    print("Connection failed")
    sys.exit(1)

# Send GET request
client.send(f"GET {file_path} HTTP/1.1\r\nHost: {server_ip}\r\n\r\n".encode())

# Receive and print response
response = client.recv(4096).decode()
print(response if "404 Not Found" not in response else "Error: File not found")

client.close()
