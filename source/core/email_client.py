"""
This module handles the creation of a secure IMAP4_SSL connection 
to an email server using the credentials provided.

It exposes a single function:

    - connect(credentials): 
        Attempts to establish an IMAP over SSL connection using the given credentials.
        On success, returns an `imaplib.IMAP4_SSL` object.
        On failure, returns a string describing the error (e.g., "Connection Failed: ...").
        
Expected keys in the `credentials` dictionary:
    - "EMAIL": User's email address
    - "PASSWORD": App-specific password or login credential
    - "HOST": IMAP server address
    - "PORT": IMAP server port (usually 993)
"""


import imaplib

def connect(credentials):
    
    try:
        mail = imaplib.IMAP4_SSL(credentials["HOST"], credentials["PORT"])
        mail.login(credentials["EMAIL"], credentials["PASSWORD"])
        return mail
    
    except Exception as e:
        return f"Connection Failed: {e}"
