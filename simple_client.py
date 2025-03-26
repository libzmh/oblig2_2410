import socket
import sys

# Read command-line arguments
if len(sys.argv) != 7 or sys.argv[1] != "-i" or sys.argv[3] != "-p" or sys.argv[5] != "-f":
    print("Usage: python3 client.py -i <server_ip> -p <server_port> -f <filename>")
    sys.exit(1)

server_ip = sys.argv[2]
server_port = int(sys.argv[4])
file_path = sys.argv[6]

# Create and connect socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

# Send HTTP GET request
client.send(f"GET {file_path} HTTP/1.1\r\nHost: {server_ip}\r\n\r\n".encode())

# Receive response
print(client.recv(4096).decode())

client.close()
