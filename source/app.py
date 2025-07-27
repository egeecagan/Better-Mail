from sys import stderr
import streamlit as st
from core import connect, return_mails_as_messages, list_senders
from gui import get_user_credentials, show_welcome
import imaplib


def main():
    st.set_page_config(page_title="BetterMail", page_icon="📬") # html title gibi dusun
    
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
                print(conn, file=stderr)
            else:
                st.session_state.conn = conn
                st.session_state.connected = True
                st.session_state.mail_addr = credentials["EMAIL"]
                st.rerun()
    else:
        conn = st.session_state.conn

        try:
            # Burada direkt INBOX seçilebilir
            conn.select("INBOX")
            st.success("Connection Successful!")

            # buraya ulasiyoruz

            print("starting seen...", file=stderr)
            seen = return_mails_as_messages(conn, search_criteria="SEEN")

            x = [m for m in seen]
            #print([m['id'] for m in seen])


            print("starting unseen...", file=stderr)
            unseen = return_mails_as_messages(conn, search_criteria="UNSEEN")

            # buraya ulasamiyoruz

            show_welcome(st.session_state.mail_addr, seen, unseen)

        except imaplib.IMAP4.abort as e:
            st.error("Connection failed!")
            st.code(str(e))
            st.session_state.connected = False
            st.rerun()


if __name__ == "__main__":
    main()
