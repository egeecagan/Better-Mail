import streamlit as st

def get_user_credentials():
    st.title("📬 Better Mail - Login")
    
    email = st.text_input("Email Address")
    password = st.text_input("App Password", type="password")
    host = st.text_input("IMAP Host", value="imap.gmail.com")
    port = st.text_input("IMAP Port", value="993")
    
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
