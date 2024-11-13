import unittest
from unittest.mock import patch, MagicMock
import socket
import client

class TestClient(unittest.TestCase):

    @patch('client.socket.socket')
    def test_start_client_send_message(self, mock_socket):
        # Arrange
        mock_client_socket = MagicMock()
        mock_socket.return_value = mock_client_socket
        
        # Simulate user input
        with patch('builtins.input', side_effect=['Hello', 'DESCONEXION']):
            client.start_client()

        # Assert that the correct messages were sent
        mock_client_socket.send.assert_any_call(b'Hello')
        mock_client_socket.send.assert_any_call(b'DESCONEXION')

        # Assert that the connection was closed
        mock_client_socket.close.assert_called_once()

    @patch('client.socket.socket')
    def test_start_client_receive_response(self, mock_socket):
        # Arrange
        mock_client_socket = MagicMock()
        mock_socket.return_value = mock_client_socket
        mock_client_socket.recv.return_value = b'HELLO'

        # Simulate user input
        with patch('builtins.input', side_effect=['Hello', 'DESCONEXION']):
            client.start_client()

        # Assert that the correct response was received and printed
        mock_client_socket.recv.assert_called_once_with(1024)

if __name__ == '__main__':
    unittest.main()