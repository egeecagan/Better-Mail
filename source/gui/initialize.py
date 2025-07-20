"""
Module for telling user how many mails did he/she received during 
the day/ week/ month. Welcome message and the total message amount
"""

import streamlit as st

def show_welcome(lst: list[int]):
    day, week, month, total, mail = lst
    st.title(f"📬 Welcome {mail}!")
    col0, col1, col2, col3 = st.columns(4)
    col0.metric("⭐️ Today", day)
    col1.metric("🗓️ Week", week)
    col2.metric("📅 Month", month)
    col3.metric("📦 Total", total)


