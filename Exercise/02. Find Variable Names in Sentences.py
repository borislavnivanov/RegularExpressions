import re

pattern = r"\b_([a-zA-Z0-9]+)\b"

text = input()

match = re.findall(pattern, text)

print(','.join(match))