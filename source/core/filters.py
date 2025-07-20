import streamlit as st
from datetime import date

def show_filters():
    st.subheader("🔍 Filter Options")

    # Filter type: Date, Sender, Subject
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
            
            start_date, end_date = st.date_input(
                "📆 Select custom date range:",
                value=(date.today(), date.today())
            )
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
        sender = st.text_input("📨 Sender email (or part of it):")
        filters["from_filter"] = sender.strip()

    elif filter_type == "By Subject":
        subject = st.text_input("📝 Subject keyword:")
        filters["subject_filter"] = subject.strip()

    else:
        st.info("Showing all emails.")

    return filters
