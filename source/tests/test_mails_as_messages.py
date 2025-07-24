import unittest
from unittest.mock import MagicMock
from email.message import Message
from core import return_mails_as_messages

class TestReturnMailsAsMessages(unittest.TestCase):

    # header ve body arasi iki adet crlf varmis 
    def setUp(self):
        self.sample_email_bytes = b"Subject: Test Mail\r\nFrom: test@example.com\r\n\r\nThis is the body."
        self.conn = MagicMock()

    def tearDown(self):
        del self.sample_email_bytes
        del self.conn

    def test_return_mails_successfully(self):
        self.conn.search.return_value = ("OK", [b"1 2"])

        self.conn.fetch.side_effect = [
            ("OK", [(b'1 (RFC822 {100}', self.sample_email_bytes)]),
            ("OK", [(b'2 (RFC822 {100}', self.sample_email_bytes)])
        ]

        result = return_mails_as_messages(self.conn)

        self.assertEqual(len(result), 2)
        self.assertTrue(all(isinstance(msg, Message) for msg in result))
        self.assertEqual(result[0]["Subject"], "Test Mail")

    def test_search_fails(self):
        # search başarısızsa
        self.conn.search.return_value = ("NO", []) # ok harici bos liste

        result = return_mails_as_messages(self.conn)
        self.assertEqual(result, [])  # Boş liste dönmeli

    def test_fetch_fails_for_one_mail(self):
        self.conn.search.return_value = ("OK", [b"1", b"2"])

        self.conn.fetch.side_effect = [
            ("OK", [(b'1 (RFC822 {100}', self.sample_email_bytes)]),
            ("NO", [])  # 2. fetch başarısız
        ]

        result = return_mails_as_messages(self.conn)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["Subject"], "Test Mail")

