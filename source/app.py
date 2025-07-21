import streamlit as st
from core import connect, return_mails_as_messages
from gui import get_user_credentials
from gui.initialize import show_welcome

def main():
    st.set_page_config(page_title="BetterMail", page_icon="📬")

    if "connected" not in st.session_state:
        st.session_state.connected = False
        st.session_state.conn = None
        st.session_state.mail_addr = ""

    if not st.session_state.connected:
        credentials = get_user_credentials()

        if credentials:
            conn = connect(credentials)
            if isinstance(conn, str):
                st.error(conn)
            else:
                st.session_state.conn = conn
                st.session_state.connected = True
                st.session_state.mail_addr = credentials["EMAIL"]
                st.rerun()
    else:
        conn = st.session_state.conn
        conn.select("INBOX")
        st.success("✅ Connection Successful!")

        seen, unseen = return_mails_as_messages(conn)

        show_welcome(st.session_state.mail_addr, seen, unseen)

if __name__ == "__main__":
    main()
