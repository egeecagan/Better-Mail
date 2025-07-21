"""
Module for telling user how many mails did he/she received during 
the day/ week/ month. Welcome message and the total message amount
"""

import streamlit as st
from core import *

def show_mail_summary(title: str, mails: list[dict]):
    st.markdown(f"### {title} ({len(mails)} mail)")
    if not mails:
        st.info("No mails.")
        return
    for mail in mails:
        st.markdown(
            f"**From:** {mail['sender']}  \n"
            f"**Subject:** {mail['subject']}  \n"
            f"**Date:** {mail['date']}"
        )
        st.markdown("---")

def show_welcome(mail_addr: str, seen: list[dict], unseen: list[dict]):
    
    st.title(f"📬 Welcome, {mail_addr}!")
    st.subheader("📊 Mail Statistics")

    filter_type = st.radio(
        "📂 Select filter:",
        ["⭐️ Today", "🗓️ This week", "📦 Total"],
        horizontal=True
    )

    match filter_type:
        case "⭐️ Today":
            filtered = filter_today(seen, unseen)
        case "🗓️ This week":
            filtered = filter_week(seen, unseen)
        case "📦 Total" | "🗂️ Show All":
            filtered = seen + unseen
        case _:
            filtered = []

    seen_filtered = [m for m in filtered if m in seen]
    unseen_filtered = [m for m in filtered if m in unseen]

    col1, col2 = st.columns(2)
    with col1:
        show_mail_summary("📖 Seen Mails", seen_filtered)

    with col2:
        show_mail_summary("📪 Unseen Mails", unseen_filtered)
