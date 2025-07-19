import imaplib

def connect(credentials):
    
    try:
        mail = imaplib.IMAP4_SSL(credentials["HOST"], credentials["PORT"])
        mail.login(credentials["EMAIL"], credentials["PASSWORD"])
        return mail
    
    except Exception as e:
        return f"Connection failed: {e}"
