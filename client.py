import socket


def start_client():
    """
    Starts the client to connect to the server and send messages.

    This function creates a TCP socket and connects it to the server 
    running on localhost at port 5000. It prompts the user to input 
    messages to send to the server. The client will continue to send 
    messages until the user types "DESCONEXION", at which point it 
    will close the connection and exit.

    The client also listens for responses from the server and prints 
    them to the console.

    Args:
        None

    Returns:
        None
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 5000))

    while True:
        message = input("Ingresa un mensaje (o 'DESCONEXION' para salir): ")
        client_socket.send(message.encode())

        if message == "DESCONEXION":
            print("Closing connection.")
            client_socket.close()
            break

        response = client_socket.recv(1024).decode()
        print(f"Server response: {response}")


if __name__ == "__main__":
    start_client()
