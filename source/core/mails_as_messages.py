"""
This module contains a single function that retrieves emails via an IMAP connection 
and converts them into `email.message.Message` objects.

These message objects (containing headers, body, and other MIME parts) are 
intended to be passed to the `parser` module in the `core` sub-package for parsing

Functions:
    - return_mails_as_messages(conn, search_criteria):
        Searches for all emails using the IMAP connection `conn` and applies the search criteria, 
        fetches each one in RFC822 format, and returns a list of parsed email message objects using 
        Python's built-in `email` library.
"""


import email


def return_mails_as_messages(conn, * ,search_criteria="ALL") -> list:
    """
    Returns list of email.message.Message objects matching the given search criteria
    
    search_criterion: str -> "ALL", "SEEN", "UNSEEN", "FROM xyz@example.com", etc.
    """
    status, messages = conn.search(None, search_criteria)
    if status != "OK":
        return []

    mail_ids = messages[0].split()
    msglist = []

    for mail_id in reversed(mail_ids):
        status, data = conn.fetch(mail_id, "(RFC822)")
        if status != "OK":
            continue
        
        raw_email = data[0][1]
        msglist.append(email.message_from_bytes(raw_email))

        # burdaki kelimeler rfc822 de email.message_from_bytes(raw_email) sonucu kullanabilecegimiz basliklar indexing gibi dictionary

        # From, To, Subject, Date, Message-ID, Reply-To, Cc, Bcc, In-Reply-To, References, Sender, Return-Path 
        # Delivered-To, Disposition-Notification-To, List-Unsubscribe, Content-Type, MIME-Version, Content-Transfer-Encoding
        # X-Mailer, X-Spam-Status, X-Priority, X-Originating-IP, X-Google-Smtp-Source, X-MS-Exchange-Organization-SCL
        # X-MS-Exchange-Organization-AuthAs, X-MS-Exchange-Organization-AuthMechanism, X-MS-Exchange-Organization-Network-Message-Id

        # Bu email.message_from_bytes(raw_email) sonucu .get_payload() body i verir onu parse etmemiz lazim

    return msglist

