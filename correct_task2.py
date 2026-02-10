import re
import pandas as pd

def count_valid_emails(emails):
    if not isinstance(emails, list):
        return 0

    s = pd.Series(emails)
    clean_s = s.dropna().astype(str).str.strip()
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    valid_emails = clean_s.str.match(email_regex)
    return valid_emails.sum()
