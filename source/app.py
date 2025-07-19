import streamlit as st
from core import connect
from gui import get_user_credentials

def main():
    user_cred = get_user_credentials()

    # if user_cred:
    #     for k in user_cred:
    #         print(f"{k}, {user_cred[k]}")

    connect(user_cred)

if __name__ == "__main__":
    main()