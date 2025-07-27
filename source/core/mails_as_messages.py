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

from sys import stderr
import email
from email.message import Message

def return_mails_as_messages(conn, *, search_criteria="ALL") -> list[Message]:
    """
    Returns list of email.message.Message objects matching the given search criteria
    """
    #print(f"imap search criterias are : {search_criteria}", file=stderr)

    status, messages = conn.search(None, search_criteria)
    if status != "OK":
        print(f"search failed: {status}", file=stderr)
        return []

    if not messages or not messages[0]:
        print("result of search is empty.", file=stderr)
        return []

    mail_ids = messages[0].split()[-10:]
    #print(f"{len(mail_ids)} mail ID's found.", file=stderr)

    msglist = []

    for mail_id in reversed(mail_ids):
        
        status, data = conn.fetch(mail_id, "(BODY.PEEK[])")
        if status != "OK":
            print(f"mail {mail_id} fetch error.", file=stderr)
            continue
        
        try:
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)

            msg['id'] = mail_id
    
            msglist.append(msg)
        except Exception as e:
            print(f"parse error: {e}", file=stderr)

    print(f"total {len(msglist)} mail recieved.", file=stderr)
    return msglist


