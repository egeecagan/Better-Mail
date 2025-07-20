"""
This module provides a Streamlit-based UI to collect user credentials 
required to connect to an IMAP email server.

It returns a dictionary containing:
    - EMAIL: The user's email address.
    - PASSWORD: An app-specific password (not the regular email password).
    - HOST: The IMAP server hostname (default: imap.gmail.com).
    - PORT: The IMAP port number (default: 993).

Note:
    - For Gmail users, app passwords are required due to security policies.
    - To generate one, enable 2-Step Verification in your Google account 
      and create an App Password.
    - For other providers, update the HOST and PORT fields accordingly.
"""


import streamlit as st

def get_user_credentials():
    st.title("📬 Better Mail - Login")
    
    email = st.text_input("Email Address")
    password = st.text_input(
        "App Password",
        type="password",
        help="""
        This password is not related to your main Gmail password.

        Gmail does not allow third-party applications like BetterMail to sign in with your regular password. 
        To use BetterMail, you need to enable 2-Step Verification in your Google Account settings and then generate an App Password.
        
        ***If you use your phone as 2FA please do not forget to remove the app password after usage***

        The App Password will be a 16-character code that you can use to sign in here.
        """
    )

    host = st.text_input("IMAP Host", value="imap.gmail.com", help="""Default Mail Provider""")
    port = st.text_input("IMAP Port", value="993", help="""Default IMAP Port""")
    
    if st.button("Connect"):
        try:
            port = int(port)
        except ValueError:
            st.error("Port must be a number!")
            return None

        return {
            "EMAIL": email,
            "PASSWORD": password,
            "HOST": host,
            "PORT": port
        }

    return None
