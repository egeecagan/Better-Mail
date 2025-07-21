import streamlit as st
from datetime import date
from core import list_senders

def show_filters(all_mails: list[dict]) -> dict:
    filter_type = st.selectbox(
        "Select filter type:",
        ["By Date", "By Sender", "By Subject", "Show All"]
    )

    filters = {}

    if filter_type == "By Date":
        date_choice = st.radio(
            "", ["⭐️ Today", "🗓️ This Week", "📅 This Month", "📦 All", "🗂️ Custom Range"],
            horizontal=True
        )

        if date_choice == "🗂️ Custom Range":
            date_range = st.date_input(
                "📆 Select custom date range:",
                value=(date.today(), date.today())
            )

            if isinstance(date_range, tuple):
                start_date, end_date = date_range
            else:
                start_date = end_date = date_range

            filters["time_filter"] = "custom"
            filters["custom_range"] = (start_date, end_date)
        else:
            filters["time_filter"] = {
                "⭐️ Today": "today",
                "🗓️ This Week": "week",
                "📅 This Month": "month",
                "📦 All": "all"
            }[date_choice]

    elif filter_type == "By Sender":
        sender_list = list_senders(all_mails)
        selected_sender = st.selectbox("📨 Select sender:", sender_list)
        filters["from_filter"] = selected_sender.strip()

    elif filter_type == "By Subject":
        subject = st.text_input("📝 Subject keyword:")
        filters["subject_filter"] = subject.strip()

    else:
        st.info("Showing all emails.")

    return filters
