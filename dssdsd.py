import re

def remove_duplicate(text):
    return re.sub(r'\b(\w+)\s+\1\b', r'\1', text)
result = remove_duplicate("i love love black metal metal")
print(result)