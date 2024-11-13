import socket
import threading


def handle_client(client_socket):
    """
    Handles communication with a specific client.

    This function runs in a separate thread and allows the server to continue
    accepting new connections. It listens for messages from the client and
    responds with the message in uppercase. If the message "DESCONEXION"
    is received, it closes the connection with that client.

    Args:
        client_socket (socket.socket): The socket object representing the
                                        connection to the client.

    Returns:
        None
    """

    while True:
        message = client_socket.recv(1024).decode()
        if message == "DESCONEXION":
            print("Closing connection with the client.")
            client_socket.close()
            break
        else:
            response = message.upper()
            client_socket.send(response.encode())


def start_server():
    """
    Starts the server to listen for incoming client connections.

    This function creates a TCP socket, binds it to the specified address and port,
    and listens for incoming connections. When a client connects, it accepts the 
    connection and starts a new thread to handle communication with that client.

    The server runs indefinitely, accepting new connections until it is manually 
    stopped.

    Args:
        None

    Returns:
        No
    """

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 5000))
    server_socket.listen(5)
    print("Server listening on localhost:5000")

    while True:
        try:
            client_socket, addr = server_socket.accept()
        except Exception as e:
            print(f"Error accepting connection: {e}")
        print(f"Connection established with {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))  # noqa: E501
        client_handler.start()


if __name__ == "__main__":
    start_server()
