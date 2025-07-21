"""
Module for telling user how many mails did he/she received during 
the day/ week/ month. Welcome message and the total message amount
"""

import streamlit as st
from core import *
import math
from .show_filters_gui import show_filters

def show_mail_summary(title: str, mails: list[dict], items_per_page: int = 10):
    """
        Represents list of mails view in my application.
        Title is either seen or unseen. Think this function creates a column
        with specified title and has mails under it
    """

    st.markdown(f"#### {title} ({len(mails)} mail)")

    if not mails:
        st.info("No mails.")
        return

    total_pages = math.ceil(len(mails) / items_per_page)
    page_key = f"{title}_page"

    if page_key not in st.session_state:
        st.session_state[page_key] = 1

    col_prev, col_info, col_next = st.columns([1, 3, 1])
    with col_prev:
        if st.button("⬅️ Prev", key=f"{title}_prev") and st.session_state[page_key] > 1:
            st.session_state[page_key] -= 1
    with col_info:
        st.markdown(f"<div style='text-align:center;'>Page {st.session_state[page_key]} of {total_pages}</div>", unsafe_allow_html=True)
    with col_next:
        if st.button("Next ➡️", key=f"{title}_next") and st.session_state[page_key] < total_pages:
            st.session_state[page_key] += 1

    page = st.session_state[page_key]
    start_idx = (page - 1) * items_per_page
    end_idx = start_idx + items_per_page

    for mail in mails[start_idx:end_idx]:
        with st.container():
            st.markdown(f"""
                <div style="background-color:#1f1f1f; padding:15px; border-radius:10px; margin-bottom:10px; border: 1px solid #333;">
                    <strong>From:</strong> <a href="mailto:{mail['sender']}" style="color:#1E90FF;">{mail['sender']}</a><br>
                    <strong>Subject:</strong> {mail['subject']}<br>
                    <strong>Date:</strong> {mail['date']}
                </div>
            """, unsafe_allow_html=True)

def show_welcome(mail_addr: str, seen: list[dict], unseen: list[dict]):
    st.title(f"📬 Welcome, {mail_addr}!")
    st.subheader("📊 Your Filtered Mail Box")

    if "show_filters" not in st.session_state:
        st.session_state["show_filters"] = True
    if "show_custom_filters" not in st.session_state:
        st.session_state["show_custom_filters"] = False

    col_toggle1, col_toggle2 = st.columns(2)
    with col_toggle1:
        entrance_clicked = st.button("🛠️ Entrance", use_container_width=True)
    with col_toggle2:
        custom_clicked = st.button("🎛️ Custom Filters", use_container_width=True)

    if entrance_clicked:
        st.session_state["show_filters"] = True
        st.session_state["show_custom_filters"] = False
    if custom_clicked:
        st.session_state["show_filters"] = False
        st.session_state["show_custom_filters"] = True

    if st.session_state["show_filters"]:
        st.markdown(
            "<div style='width: 100%; max-width: 1000px; margin: auto;'>", unsafe_allow_html=True
        )

        filter_type = st.radio(
            "",
            ["⭐️ Today", "🗓️ This week", "📦 Total"],
            horizontal=True
        )

        match filter_type:
            case "⭐️ Today":
                filtered = filter_today(seen, unseen)
            case "🗓️ This week":
                filtered = filter_week(seen, unseen)
            case _:
                filtered = seen + unseen

        seen_filtered = [m for m in filtered if m in seen]
        unseen_filtered = [m for m in filtered if m in unseen]

        col1, col2 = st.columns(2)
        with col1:
            show_mail_summary("📖 Seen Mails", seen_filtered)
        with col2:
            show_mail_summary("📪 Unseen Mails", unseen_filtered)

        st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state["show_custom_filters"]:

        filters = show_filters(seen + unseen)

        filtered = filter_mails(filters, seen, unseen)

        seen_filtered = [m for m in filtered if m in seen]
        unseen_filtered = [m for m in filtered if m in unseen]

        col1, col2 = st.columns(2)
        with col1:
            show_mail_summary("📖 Seen Mails", seen_filtered)
        with col2:
            show_mail_summary("📪 Unseen Mails", unseen_filtered)
        
        st.markdown("</div>", unsafe_allow_html=True)
