"""
This module contains a single function that retrieves emails via an IMAP connection 
and converts them into `email.message.Message` objects and returns them in a list.

These message objects (containing headers, body, and other MIME parts) are 
intended to be passed to the `parser` module in the `core` sub-package for parsing.

Functions:
    - return_mails_as_messages(conn, search_criteria):
        Searches for all emails using the IMAP connection `conn` and applies the search criteria, 
        fetches each one in RFC822 format, and returns a list of parsed email message objects using 
        Python's built-in `email` library.
"""


import email
from email.message import Message

def return_mails_as_messages(conn, * ,search_criteria="ALL") -> list[Message]:
    """
    Returns list of email.message.Message objects matching the given search criteria
    
    search_criterion: str -> "ALL", "SEEN", "UNSEEN", "FROM xyz@example.com", etc.
    """
    status, messages = conn.search(None, search_criteria)
    if status != "OK":
        return []

    mail_ids = messages[0].split()
    msglist = []
    
    ## buraya geliyor

    for mail_id in reversed(mail_ids):
        status, data = conn.fetch(mail_id, "(RFC822)")
        if status != "OK":
            continue
        
        raw_email = data[0][1]
        msglist.append(email.message_from_bytes(raw_email))

        # email.message_from_bytes ile elde edilen nesne, başlıklara sözlük gibi erişim sağlar (case-insensitive).

        # Kullanılabilecek başlıklar örnekleri: From, To, Subject, Date, Message-ID, Reply-To, Cc, Bcc, Content-Type, vb.
        # Bunlara msg["From"], msg.get("Subject") gibi erişilir.

    return msglist

