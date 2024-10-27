import re

def extract_hashtags(text):
    return re.findall(r'#\w+', text)

result = extract_hashtags("#сигма, #вуменмомент, тайлердерде")
print(result)