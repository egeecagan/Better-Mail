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
        "Application Password",
        type="password",
        help="""
        This password is not related to your main Gmail password.

        Gmail does not allow third-party applications like BetterMail to sign in with your regular password. 
        To use BetterMail, you need to enable 2-Step Verification in your Google Account settings and then generate an App Password.
        
        ***If you use your phone as 2FA please do not forget to remove the app password after usage***

        The App Password will be a 16-character code that you can use to sign in here.
        """
    )

    st.warning("This app only supports IMAP. POP3 will not work.")

    host_options = {
        "Gmail": "imap.gmail.com",
        "Outlook / Office365": "outlook.office365.com",
        "Yahoo Mail": "imap.mail.yahoo.com",
        "iCloud (Apple Mail)": "imap.mail.me.com",
        "Yandex Mail": "imap.yandex.com",
        "Zoho Mail": "imap.zoho.com",
        "Other (Manual Entry)": "manual"
    }

    port_options = {
        "Default (SSL, 993)": 993,
        "Old (STARTTLS, 143)": 143,
        "Manual entry": "manual"
    }

    provider = st.selectbox("Choose your email provider", list(host_options.keys()))
    selected_host = host_options[provider]

    if selected_host == "manual":
        host = st.text_input("Enter your IMAP host manually")
    else:
        host = selected_host
        st.markdown(f"Using host: `{host}`")

    port = st.selectbox("Choose your IMAP port", list(port_options.keys()))
    selected_port = port_options[port]
    


    if selected_port == "manual":
        port = st.text_input("Enter your IMAP port manually")
    else:
        port = selected_port
        st.markdown(f"Using port: `{port}`")
    
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
