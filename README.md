# 📬 Better Mail

A tool for consumers to group who sent mails to them and see them in a list.

## 🚨 Main Problem

I receive a large number of emails from various individuals and companies. Over time, it's become difficult to keep track of how many unique senders I interact with and which mailing lists or subscriptions I'm currently signed up for.

The goal of this project is to analyze my inbox in order to:

- Identify how many unique senders have contacted me.
- And group senders to additional folders for who are they.
- Detect and list all email subscriptions or newsletter-type emails.

Since I couldn't find any existing tool or service that provides a clear overview of this information, I decided to build my own solution (it is free 😝). Also i thought it would be fun to code this project because it solves a real life problem of mine.

## How to use

1. Move your working directory into the main project 
   folder if your folder is in desktop do `cd bettermail`

2. Create a venv with `python -m venv venv` and then `source venv/bin/activate`

3. Install the requirements in the requirements.txt folder with `pip`

4. Use `cd source`

5. Use `streamlit run app.py` and follow the instructions
   on the graphical user interface

## 🛠️ Technologies Used

- **python 3 (3.13.4)**
- **streamlit**           - for graphical user interface on web without frontend knowledge
- **git cli**             - for centralized version control ( to be real only for learning purposes)

## ⚙️ Packages Used (builtin)

- **email**               – for parsing and handling email message structures
- **imaplib**             – for connecting to and interacting with mail servers via IMAP
- **unittest**            – for testing the application
- **virtual environment** – for creating an isolated development environment
