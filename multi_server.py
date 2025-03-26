from socket import *
import _thread as thread
import time
import sys


def now():
    """Returns the current time."""
    return time.ctime(time.time())


def handleClient(connectionSocket):
    """Handles a single client request."""
    try:
        request = connectionSocket.recv(2000).decode()
        print("Received request:\n", request)

        headers = request.split('\n')
        first_line = headers[0].split()

        if len(first_line) < 2:
            connectionSocket.close()
            return

        http_method = first_line[0]
        path = first_line[1]

        if http_method == 'GET' and path == '/index.html':
            try:
                with open('index.html', 'r') as fin:
                    content = fin.read()
                response = 'HTTP/1.1 200 OK\r\n\r\n' + content
            except FileNotFoundError:
                response = 'HTTP/1.1 404 Not Found\r\n\r\n<h1>404 Not Found</h1>'
        else:
            response = 'HTTP/1.1 404 Not Found\r\n\r\n<h1>404 Not Found</h1>'

        connectionSocket.sendall(response.encode())

    except Exception as e:
        print(f"Error: {e}")
    finally:
        connectionSocket.close()


def main():
    """Creates a server socket, listens for connections, and spawns new threads for clients."""
    serverPort = 8080
    serverSocket = socket(AF_INET, SOCK_STREAM)

    try:
        serverSocket.bind(('', serverPort))
    except Exception as e:
        print(f"Bind failed. Error: {e}")
        sys.exit()

    serverSocket.listen(5)
    print(f'The server is ready to receive on port {serverPort}')

    while True:
        connectionSocket, addr = serverSocket.accept()
        print('Server connected by', addr)
        print('At', now())

        # Spawn a new thread for each client
        thread.start_new_thread(handleClient, (connectionSocket,))

    serverSocket.close()


if __name__ == '__main__':
    main()
