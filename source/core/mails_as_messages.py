"""
This module contains a single function that retrieves emails via an IMAP connection 
and converts them into `email.message.Message` objects.

These message objects (containing headers, body, and other MIME parts) are 
intended to be passed to the `parser` module in the `core` sub-package for further processing.

Functions:
    - return_mails_as_messages(conn) -> list[Message]:
        Searches for all emails using the IMAP connection `conn`, fetches each one in RFC822 format, 
        and returns a list of parsed email message objects using Python's built-in `email` library.
"""


import email

def return_mails_as_messages(conn) -> list[dict]:
    status, messages = conn.search(None, "ALL") # NONE charset = utf-8 demek ALL ise kriterler
    if status != "OK":
        return []

    mail_ids = messages[0].split()  # messages bir liste ama icinde sadece 1 eleman var [b'1 2 3 4 5'] gibi
    # 0 index olarak tek eleman oldugu icin onu alir

    msglist = []

    for mail_id in reversed(mail_ids):
        status, data = conn.fetch(mail_id, "(RFC822)")
        if status != "OK":
            continue

        raw_email = data[0][1] # gene tek elemanli iterable 0,0 ise header gereksiz bizim icin
        msglist.append(email.message_from_bytes(raw_email))

    return msglist
