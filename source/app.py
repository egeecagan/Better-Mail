import streamlit as st
from core import connect
from gui import get_user_credentials
from core import return_mails_as_messages

def main():
    st.set_page_config(page_title="BetterMail", page_icon="📬")

    if "connected" not in st.session_state:
        st.session_state.connected = False
        st.session_state.conn = None

    if not st.session_state.connected:
        credentials = get_user_credentials()

        if credentials:
            conn = connect(credentials)
            if isinstance(conn, str):
                st.error(conn)
                # eger str ise hata 
            else:
                st.session_state.conn = conn
                st.session_state.connected = True
                st.rerun()
    else:
        conn = st.session_state.conn
        conn.select("INBOX")
        st.success("Connection Succesfull!")
        

    


if __name__ == "__main__":
    main()