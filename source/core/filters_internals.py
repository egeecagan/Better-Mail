from datetime import datetime, timedelta 
from utils import parse_date

def filter_today(seen: list[dict], unseen: list[dict]) -> list[dict]:
    today = datetime.now().date()
    all_mails = seen + unseen
    return [mail for mail in all_mails if parse_date(mail["date"]).date() == today]

def filter_week(seen: list[dict], unseen: list[dict]) -> list[dict]:
    today = datetime.now().date()
    week_ago = today - timedelta(days=7)
    all_mails = seen + unseen
    return [mail for mail in all_mails if week_ago <= parse_date(mail["date"]).date() <= today]

def filter_mails(filter_: dict, seen: list[dict], unseen: list[dict]):  # list of dictionaries a dict contains sender subject body etc.
    match filter_:
        case:
            pass

def filter_custom_range():
    pass

def list_senders(all: list[dict]) -> list[dict]:
    pass