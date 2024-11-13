import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen(5)
    print("Server listening on localhost:5000")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection established with {addr}")
        
        while True:
            message = client_socket.recv(1024).decode()
            if message == "DESCONEXION":
                print("Closing connection with the client.")
                client_socket.close()
                break
            else:
                response = message.upper()
                client_socket.send(response.encode())

if __name__ == "__main__":
    start_server()