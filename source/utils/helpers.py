from datetime import datetime

def parse_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

# will use the return value weith .date() method