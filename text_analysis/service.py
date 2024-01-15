import re


def letter_verification(string):
    return bool(re.search(r"[a-zA-Z]", string))
