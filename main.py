import re

def valid_email(email):
    pattern = r'^[\w\.-]+@[\w.-]+\.[a-zA-Z]{2,6}$'
    return re.match(pattern, email) is not None

print(valid_email("xu@gmail.com"))