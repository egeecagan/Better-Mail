import unittest
from unittest.mock import patch, MagicMock
import imaplib

from core import connect

class TestEmailClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.shared_credentials = {
            "HOST": "imap.example.com",
            "PORT": 993,
            "EMAIL": "test@example.com",
            "PASSWORD": "correct_password"
        }
        print("shared_credentials has been defined")

    @classmethod
    def tearDownClass(cls):
        del cls.shared_credentials
        print("shared credentials has been deleted")

    @patch("core.email_client.imaplib.IMAP4_SSL")    # bu decorator email_client dosyasi importtan gelen fonksiyonu mock lar
    def test_successful_connection(self, mock_imap): # yani artik mock_imap(...) = imaplib.IMAP4_SSL(...)
        mock_instance = MagicMock() # <- bu mail objesi aslinda
        mock_imap.return_value = mock_instance
        
        result = connect(self.shared_credentials)  # bunu calistirdigimiz an icindeki imap li fonsiyon mock imapi cagirir
        # bunun icinde login shared credentials ile cagirilacak
    
        mock_imap.assert_called_with("imap.example.com", 993)  
        # bu mock_imap fonksiyon degerleriyle cagirildi mi o test edilir

        mock_instance.login.assert_called_with("test@example.com", "correct_password")
        self.assertEqual(result, mock_instance)

    @patch("core.email_client.imaplib.IMAP4_SSL", side_effect=Exception("Connection refused"))
    # bu IMAP4_SSL(...) cagirildigi anda Exception("Conn..") firlatacagini soyler bu patch
    def test_connection_failure(self, mock_imap):
        result = connect(self.shared_credentials)
        self.assertTrue(result.startswith("Server connection failed:"))
        self.assertIn("Connection refused", result) # Exception icinde bu var

    @patch("core.email_client.imaplib.IMAP4_SSL")
    def test_login_failure(self, mock_imap):
        mock_instance = MagicMock()
        mock_instance.login.side_effect = imaplib.IMAP4.error("Invalid credentials")
        mock_imap.return_value = mock_instance

        result = connect(self.shared_credentials)
        self.assertTrue(result.startswith("Login failed:"))
        self.assertIn("Invalid credentials", result)

    @patch("core.email_client.imaplib.IMAP4_SSL")
    def test_unexpected_login_error(self, mock_imap):
        mock_instance = MagicMock()
        mock_instance.login.side_effect = Exception("Timeout")
        mock_imap.return_value = mock_instance

        result = connect(self.shared_credentials)
        self.assertTrue(result.startswith("Unexpected login error:"))
        self.assertIn("Timeout", result)

if __name__ == '__main__':
    unittest.main()
