import socket

def main():
    port = 8080
    server_ip = '127.0.0.1'
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((server_ip, port))
    server_socket.listen(5)
    print(f'listening on port {port} ...')

    while True:
        client_socket, client_address = server_socket.accept()
        request = client_socket.recv(2000).decode()
        print(request)
        headers = request.split('\n')
        first_header_component = headers[0].split()
        http_method = first_header_component[0]
        path = first_header_component[1]

        if path == '/index.html':
            fin = open('index.html')
            content = fin.read()
            fin.close()
            response = 'HTTP/1.1 200 OK \n\n' + content
        else:
            response = 'HTTP/1.1 404 Not Found \n\n<h1>404 Not Found</h1>'

        client_socket.sendall(response.encode())
        client_socket.close()

if __name__ == "__main__":
    main()
