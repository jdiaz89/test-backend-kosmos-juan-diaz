import unittest
from unittest.mock import patch, MagicMock
import server  # Asegúrate de que este es el nombre correcto de tu archivo

class TestServer(unittest.TestCase):

    @patch('server.socket.socket')
    def test_start_server_accepts_connections(self, mock_socket):
        # Simular el socket del servidor
        mock_server_socket = MagicMock()
        mock_socket.return_value = mock_server_socket
        
        # Simular un socket de cliente
        mock_client_socket = MagicMock()
        mock_server_socket.accept.return_value = (mock_client_socket, ('localhost', 5000))

        # Ejecutar el servidor en un hilo para evitar que se quede colgado
        with patch('builtins.print') as mock_print:
            server.start_server()

        # Verificar que se aceptó una conexión
        mock_server_socket.accept.assert_called_once()
        mock_print.assert_called_with("Connection established with ('localhost', 5000)")

if __name__ == '__main__':
    unittest.main()