from datetime import date, datetime, timedelta 
from utils import parse_date, decode_and_escape
from email.utils import parseaddr
from dateutil.relativedelta import relativedelta  # A month can ne 28, 29, 30, 31 days

def filter_today(seen: list[dict], unseen: list[dict]) -> list[dict]:
    """
    Filters emails received today from both seen and unseen lists.
    """
    today = datetime.now().date()
    all_mails = seen + unseen
    return [mail for mail in all_mails if parse_date(mail["date"]).date() == today]

def filter_week(seen: list[dict], unseen: list[dict]) -> list[dict]:
    """
    Filters emails received within the last 7 days (inclusive).
    """
    today = datetime.now().date()
    week_ago = today - timedelta(days=7)
    all_mails = seen + unseen
    return [mail for mail in all_mails if week_ago <= parse_date(mail["date"]).date() <= today]

def filter_month(seen: list[dict], unseen: list[dict]) -> list[dict]:
    """
    Filters emails received within the last 1 month (inclusive).
    Uses relativedelta to handle varying month lengths (28-31 days).
    """
    today = datetime.now().date()
    month_ago = today - relativedelta(months=1)
    all_mails = seen + unseen
    return [mail for mail in all_mails if month_ago <= parse_date(mail["date"]).date() <= today]

def filter_custom_range(mails: list[dict], start_date: date, end_date: date) -> list[dict]:
    """
    Filters emails within a custom date range.
    """
    return [
        mail for mail in mails
        if start_date <= parse_date(mail["date"]).date() <= end_date
    ]

def filter_mails(filter_: dict, seen: list[dict], unseen: list[dict]) -> list[dict]:
    """
    Applies a filter to the given seen and unseen email lists.
    filter_ is a dict keys can be ["time_filter": "today, week month, all"
    , "custom_range", "from_filter", "subject_filter"]
    """
    all_mails = seen + unseen

    if not filter_:
        return all_mails

    if "time_filter" in filter_:
        match filter_["time_filter"]:
            case "today":
                return filter_today(seen, unseen)
            case "week":
                return filter_week(seen, unseen)
            case "month":
                return filter_month(seen, unseen)
            case "all":
                return all_mails
            case "custom":
                start, end = filter_["custom_range"]
                return filter_custom_range(all_mails, start, end)

    elif "from_filter" in filter_:
        sender_query = filter_["from_filter"].lower()
        return [mail for mail in all_mails if sender_query in mail["from"].lower()]

    elif "subject_filter" in filter_:
        subject_query = filter_["subject_filter"].lower()
        return [mail for mail in all_mails if subject_query in decode_and_escape(mail["subject"]).lower()]
    return all_mails

def list_senders(all_mails: list[dict]) -> set[str]:
    """
    Extracts and returns a sorted set of unique sender email addresses.
    all_mails is seen + unseen mail list. If streamlit creates a problem in future
    i will make thiss function to return a csv file for senders
    """
    senders = []
    for mail in all_mails:
        raw_from = mail.get("from")
        if raw_from:
            name, addr = parseaddr(raw_from)
            if addr:  
                senders.append(addr)
    return sorted(set(senders))

