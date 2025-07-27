"""
This module handles the creation of a secure IMAP4_SSL connection 
to an email server using the credentials provided.

It exposes a single function:

    - connect(credentials: a dictionary containing user information): 
        Attempts to create an IMAP over SSL connection using the given credentials.
        On success, returns an `imaplib.IMAP4_SSL` object.
        On failure, returns a string describing the error (e.g., "Connection Failed: ...").
"""

import imaplib
from typing import Union

def connect(credentials) -> Union[imaplib.IMAP4_SSL, str]: # Union in typing is to tell this function can return 2 different type
    
    try:
        mail = imaplib.IMAP4_SSL(credentials["HOST"], credentials["PORT"])
    except Exception as e:
        return f"Server connection failed: {e}"

    try:
        mail.login(credentials["EMAIL"], credentials["PASSWORD"])
    except imaplib.IMAP4.error as e:
        return f"Login failed: {e}"
    except Exception as e:
        return f"Unexpected login error: {e}"

    return mail