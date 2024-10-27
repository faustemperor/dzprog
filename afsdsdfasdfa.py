import re

def extract_phone_numbers(text):
    pattern = r'$\d{3}$\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4}'
    return re.findall(pattern, text)

result = extract_phone_numbers("(123) 456-7890 и 123-456-7890.")
print(result)