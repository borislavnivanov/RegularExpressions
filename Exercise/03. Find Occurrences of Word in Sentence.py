import re

text = input()
check = input()
pattern = rf'\b{check}\b'

matches = re.findall(pattern, text, re.IGNORECASE)

print(len(matches))
