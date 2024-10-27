import re

def replace_date(text):
    pattern = r'(\d{2})/(\d{2})/(\d{4})'
    return re.sub(pattern,r'\3-\2-\1', text)

result = replace_date("сегодня 24/10/2025.")
print(result)