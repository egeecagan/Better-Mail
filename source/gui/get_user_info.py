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
