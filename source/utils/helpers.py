from email.utils import parsedate_to_datetime
from email.header import decode_header
from datetime import datetime
import re

def parse_date(date_str: str) -> datetime:
    """
    Parses a date string from an email header into a datetime object.

    parse_date("Thu, 25 Jul 2025 20:15:33 +0000")
    datetime.datetime(2025, 7, 25, 20, 15, 33, tzinfo=...)
    """
    try:
        return parsedate_to_datetime(date_str)
    except Exception as e:
        print(f"❌ parse_date error: {e}")
        return datetime.min

def decode_mime_words(header_value):
    """
    Decodes MIME encoded words in an email header field (Subject, From...).

    Email headers may include non-ASCII characters encoded using RFC 2047 
    MIME encoding (e.g., "=?UTF-8?Q?Test_=C3=BCber_Subject?=").
    """
    decoded_parts = decode_header(header_value)
    return ''.join(
        part.decode(encoding or 'utf-8') if isinstance(part, bytes) else part
        for part, encoding in decoded_parts
    )

def is_encoded_subject(subject: str) -> bool:
    """
    Checks whether a given email subject line is MIME-encoded (RFC 2047).
    """
    return bool(re.search(r"=\?.*\?.*\?.*\?=", subject))
