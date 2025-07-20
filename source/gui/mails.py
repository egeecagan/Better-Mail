import streamlit as st
import email

def show_mailbox(conn):
    st.subheader("📥 Gelen Kutusu")

    status, messages = conn.search(None, "ALL")
    if status != "OK":
        st.error("Mailler alınamadı.")
        return

    mail_ids = messages[0].split()[-10:]  # son 10 mail
    for mail_id in reversed(mail_ids):
        status, data = conn.fetch(mail_id, "(RFC822)")
        if status != "OK":
            st.warning(f"Mail alınamadı: {mail_id}")
            continue

        raw_email = data[0][1]
        msg = email.message_from_bytes(raw_email)

        subject = msg["subject"]
        from_ = msg["from"]
        date = msg["date"]

        with st.expander(f"📩 {subject} — {from_} — {date}"):
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    if content_type == "text/plain":
                        payload = part.get_payload(decode=True)
                        if payload:
                            body += payload.decode(errors="ignore")
            else:
                payload = msg.get_payload(decode=True)
                if payload:
                    body += payload.decode(errors="ignore")

            st.text(body if body else "[Boş içerik]")

    if st.button("🔌 exit"):
        st.session_state.connected = False
        st.session_state.conn = None
        st.rerun()